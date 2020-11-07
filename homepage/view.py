from pathlib import Path
from zipfile import ZipFile

import sys
import tempfile


def main():
    directory = "."
    if len(sys.argv) > 1:
        directory = sys.argv[1]

    directory = Path(directory)

    files = directory.glob("*.zip")
    with tempfile.TemporaryDirectory() as tempdir:
        for fi in files:
            z = ZipFile(fi)
            z.extractall(tempdir)

            input("Press any key when ready for next submission. ")

            z.close()


if __name__ == "__main__":
    main()
