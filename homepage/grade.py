# Autograde correctness for homepage
from bs4 import BeautifulSoup
from html5validator import Validator
from pathlib import Path 
from io import StringIO
from urllib.parse import urlparse
from zipfile import ZipFile

import contextlib
import csv
import logging
import re
import requests
import sys
import tempfile
import tinycss2
import yaml


EXCEPTED_TAGS = ["html", "head", "body", "title"]
BOOTSTRAP_URL = "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
SUBMISSION_SUBDIRECTORY = "homepage"

def check_script(c, tempdir):
    # If inline script
    if not c.has_attr("src"):
        content = c.string
        if content.strip() != "":
            return True

    else:
        p = ""

        # If relative (local)
        if not urlparse(c.get("src")).netloc:
            p = c.get("src")
        elif "cs50.xyz" in c.get("src"):
            p = urlparse(c.get("src")).path
        else:
            return False

        try:
            # Gradescope has subdirectory for submission itself
            with open(Path(tempdir) / SUBMISSION_SUBDIRECTORY / p) as f:
                content = f.read()
                if content.strip() != "":
                    return True
        except:
            pass

        try:
            with open(Path(tempdir) / p) as f:
                content = f.read()
                if content.strip() != "":
                    return True
        except:
            return False


def get_bootstrap_classes():
    """Get a set of Bootstrap classes (and technically, any non-tag identifiers)."""
    r = requests.get(BOOTSTRAP_URL)
    css = r.text
    styles = tinycss2.parse_rule_list(css, skip_comments=True, skip_whitespace=True)

    classes = set()

    for style in styles:
        if style.type == "qualified-rule":
            if not isinstance(style.prelude[0], tinycss2.ast.IdentToken):
                classes.add(tinycss2.serialize(style.prelude))

    return classes


def grade(f, bootstrap_classes):
    """Grade an individual submission"""
    z = ZipFile(f)
    print(str(f))

    requirements = {
        "index.html": False,
        "page_count": 0,
        "html_errors": 0,
        "html_validator_log": "",
        "unique_tags": set(),
        "bootstrap_classes": set(),
        "stylesheet": False,
        "css_selectors": set(),
        "css_selectors_with_5": 0,
        "nonempty_script": False
    }

    html = list()
    css = list()
    js = list()

    for item in z.namelist():
        if re.match(".*\.html$", item) and "__MACOSX/" not in item:
            html.append(item)
            requirements["index.html"] = requirements["index.html"] or (re.match(".*index\.html$", item) is not None)

        elif re.match(".*\.css$", item) and "__MACOSX/" not in item:
            css.append(item)
            requirements["stylesheet"] = True

        elif re.match(".*\.js$", item) and "__MACOSX/" not in item:
            js.append(item)

    requirements["page_count"] = len(html)
    
    with tempfile.TemporaryDirectory() as tempdir:
        # Extract
        z.extractall(tempdir)
        td = Path(tempdir)

        # Mac fix
        macosx = False
        for item in z.namelist():
            if item.startswith("__MACOSX/"): # Here we pray nobody purposely makes a directory like this
                macosx = True

        if macosx:
            sub_id = str(f).split(".")[0].replace("/mounted/", "")
            td = td / sub_id

        html_paths = [Path(tempdir) / h for h in html]
        css_paths = [Path(tempdir) / h for h in css]

        # Get student info
        try:
            with open(td / "metadata.yml") as f:
                lines = f.readlines()
                data = yaml.load(bytes("\n".join(lines[0:5]), encoding="utf8"), Loader=yaml.Loader)
                requirements["submission_id"] = data[":id"]
                requirements["student_name"] = data[":submitters"][0][":name"]
                requirements["student_email"] = data[":submitters"][0][":email"]
        except:
            requirements["submission_id"] = ""
            requirements["student_name"] = str(f)
            requirements["student_email"] = ""
        
        # Validate
        validator = Validator()
        log = "/mounted/log.txt"
        logging.basicConfig(filename=log)

        requirements["html_errors"] = validator.validate(html_paths)

        with open("/mounted/log.txt", "r") as f:
            requirements["html_validator_log"] = f.read()
        open("/mounted/log.txt", "w").close()


        # HTML files
        for h in html_paths:
            print(h)
            with open(h) as f:
                soup = BeautifulSoup(f, 'html.parser')
                for c in soup.descendants:
                    if c.name is not None and c.name not in EXCEPTED_TAGS:
                        requirements["unique_tags"].add(c.name)

                    # JavaScript
                    if c.name == "script":
                        requirements["nonempty_script"] = requirements["nonempty_script"] or check_script(c, td)

                    # Bootstrap classes
                    try:
                        if c.has_attr("class"):
                            contains = set(c.get("class"))
                            contains = set([f".{ct}" for ct in contains])
                            requirements["bootstrap_classes"] = requirements["bootstrap_classes"].union(contains.intersection(bootstrap_classes))
                    except:
                        pass
                            
        # CSS files
        for s in css_paths:
            with open(s) as f:
                text = f.read()
            styles = tinycss2.parse_stylesheet(text, skip_comments=True, skip_whitespace=True)
            for style in styles:
                if isinstance(style, tinycss2.ast.QualifiedRule):
                    requirements["css_selectors"].add(tinycss2.serialize(style.prelude))
                    if len(tinycss2.parse_declaration_list(style.content, skip_comments=True, skip_whitespace=True)) >= 5:
                        requirements["css_selectors_with_5"] += 1

    return requirements


def calculate_grades(grades):
    """Calculates correctness grades."""

    calculated = list()
    for grade in grades:

        # up to 2.5 points for HTML, 1.5 points for CSS, 1 point for JS
        html_score = .5 * grade["index.html"] \
                    + min(.5, grade["page_count"] / 4 * .5) \
                    + max(0, .5 - .05 * grade["html_errors"]) \
                    + min(.5, .5 * len(grade["unique_tags"]) / 10) \
                    + .5 * (len(grade["bootstrap_classes"]) > 0)
        css_score = .5 * grade["stylesheet"] \
                    + min(.5, .5 * len(grade["css_selectors"]) / 5) \
                    + min(.5, .5 * grade["css_selectors_with_5"] / 5)
        js_score = 1 * grade["nonempty_script"]

        total = html_score + css_score + js_score

        calculated.append({
            "submission_id": grade["submission_id"],
            "student_name": grade["student_name"],
            "student_email": grade["student_email"],
            "total": total,
            "html": html_score,
            "css": css_score,
            "js": js_score
        })

    return calculated


def main():
    directory = "."
    if len(sys.argv) > 1:
        directory = sys.argv[1]

    directory = Path(directory)

    files = directory.glob("*.zip")
    bootstrap_classes = get_bootstrap_classes()
    grades = list()
    for f in files:
        grades.append(grade(f, bootstrap_classes))

    compiled = calculate_grades(grades)

    if len(compiled) < 1:
        print("No ZIP files.")
        return

    with open("/mounted/grades.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=compiled[0].keys())
        writer.writeheader()
        writer.writerows(compiled)

    print("Completed grading.")
    

if __name__ == "__main__":
    main()
