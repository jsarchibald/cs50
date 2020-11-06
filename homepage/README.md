# Homepage autograder

Make sure you have Docker.

## Usage

Make sure you have Docker, and Docker is running. Download the image by running the following in your terminal:

```
docker pull jarchibald/homepage-grader:latest
```

While that's working, download (into a new folder) all your students' submissions as ZIP files from Gradescope. Easiest is probably to click the section number for the first submission from your section to filter out everyone else. Then, on the individual submission page, click "View Submission" (it's next to "Autograder results"). Then click "Download submission" on the page that opens. Close that page's tab, and use the right arrow key to go to the next submission. Repeat the ZIP download.

Open the Docker desktop interface. Go to Settings (gear icon). Click Resources, then File Sharing. Click the blue plus button, then navigate to the new folder where your ZIP files are located to allow Docker to share that folder with the container.

When the `docker pull` is done, navigate in a terminal to the folder where your ZIP files are located. Then run the following command (varies by your computer's operating system):

```
Windows:
docker run -it -v %cd%:/mounted jarchibald/homepage-grader

Mac, Linux:
docker run -it -v ${PWD}:/mounted jarchibald/homepage-grader
```

When it says "Completed grading" check in the folder where the ZIPs are located for `grades.csv`. Each row should have a student's name, email, submission ID number, and total score for correctness as well as a breakdown of HTML, CSS, and JS scores.


## Setup for development

Download repo, cd into `homepage` directory within.

To build:

```
docker build -t homepage .
```

Then, go to `Docker Settings / Resources / File Sharing` and add the folder in which you're going to save students' submission ZIP files.

To run:

1. Download the ZIPs of all your students' submissions into one folder.
2. Run `docker run -it -v <folder>:/mounted homepage` where `<folder>` corresponds to the full directory path to the folder where you downloaded the submissions.
3. Find results in `grades.csv`.