# Homepage autograder

Make sure you have Docker.

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