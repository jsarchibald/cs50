# Week 6 Exercises

Exercises designed by Josh Archibald for the section of [week 6 of CS50](https://cs50.harvard.edu/college/weeks/6).

Exercises can be completed using [this CS50 Sandbox](http://bit.ly/31A4fpI).


## Smoots

One [chilly October night in 1958](https://en.wikipedia.org/wiki/Smoot), some fraternity brothers down the street decided they wanted to measure the [Harvard Bridge](https://goo.gl/maps/mLuJKgjXywX1mAhX6) (the bridge near MIT where Mass Ave crosses into Boston). To make it fun, they used the height of the shortest member - [Oliver Smoot](https://en.wikipedia.org/wiki/Oliver_R._Smoot) - as the unit of measurement and marked significant locations with paint. (Fun fact: Smoot went on to chair the American National Standards Institute and serve as president of the International Organization for Standardization.)

![Smoots](http://web.mit.edu/smoot/backg0.jpg "Smoots")

The Smoot measurements are repainted every few years by MIT students, so you can still see them today! (Visit MIT sometime; it's a nice campus and you can take classes there.)

**One chilly October night in 2019**, Asia, Chris, and Erik decide to race from the MIT side of the bridge to Boston. Whoever finishes first doesn't have to help pay for dinner on Newbury Street. Being MIT students, they have affixed to their ankles devices they manufactured in [2.009](http://web.mit.edu/2.009/www/index.html) (see [here](https://www.youtube.com/watch?v=J-ToBoJWVlg) for an amusing video featuring the class's professor) which record each runner's time, distance, velocity, and acceleration randomly.

Let's write some Python to predict who is the winner based on the data saved in `race.csv`. Some parameters for these data: each person can only have one data point recorded; if multiple points are available, use the last one in the file. Each point will store the time and the person's position, velocity, and acceleration (all of these will use Smoots as the unit of measurement for distance rather than meters or feet).

### Usage

Most of the usage details are handled for you in `race.py`. Read through that file to gain an understanding of how to check argv and call functions from `helpers.py`.

```
python race.py <datafile.csv>
```

### Background

Ultimately, we're looking to find who has the shortest time *t* to finish the race, because the person who takes the least time to run across the bridge is the winner.

![Kinematic formulas](https://www.physicsclassroom.com/Class/1DKin/U1L6a1.gif "Kinematic formulas")

Algebra-based physics gives us these kinematic formulas to work with, where *d* is displacement of an object, *v* is its velocity (i and f indicate initial and final velocities, respectively), *a* is its acceleration, and *t* is the change in time during the object's movement.

![The math for time](https://latex.codecogs.com/gif.latex?t%3D%5Cfrac%7B2d%7D%7Bv_%7Bi%7D%20&plus;%20v_%7Bf%7D%7D "The math for time")

To find the time to completion from a given point, we need to use the formula on the bottom right. When we rearrange the formula, we see that we need *vf* as well - can calculate this using the formula on the top right.

![The math for velocity](https://latex.codecogs.com/gif.latex?v_%7Bf%7D%20%3D%20%5Csqrt%7Bv_%7Bi%7D%5E2%20&plus;%202ad%7D "The math for velocity")

Remember that the time we calculate here will only be for the remainder of the race from that point -- we'll need to add the time it took to get to that point to get the total time.

Finally, we'll save each runner's total time, average velocity, and final velocity to a file named `stats.csv` and print out a message indicating who probably won the race.

The code in `race.py` does much of the heavy lifting for us. We just need to write some helper functions.


### Final velocity

Write a function `final_velocity(a, d, vi)` that takes in an initial velocity, acceleration, and distance to the end of the bridge and returns the person's final velocity.

![The math for velocity](https://latex.codecogs.com/gif.latex?v_%7Bf%7D%20%3D%20%5Csqrt%7Bv_%7Bi%7D%5E2%20&plus;%202ad%7D "The math for velocity")

### Time

Write a function `time(d, vi, vf)` that takes in a distance to the end, initial velocity, and final velocity and returns the amount of time to cover that distance.

![The math for time](https://latex.codecogs.com/gif.latex?t%3D%5Cfrac%7B2d%7D%7Bv_%7Bi%7D%20&plus;%20v_%7Bf%7D%7D "The math for time")

### Smoots to meters

All of the measurements in `race.csv` were in Smoots. Write a function `s_to_m(smoots)` to convert Smoots to meters. (Hint: there are `1.078` meters in a Smoot.)

![The math for Smoots to meters](https://latex.codecogs.com/gif.latex?m%20%3D%201.078s "The math for Smoots to meters")

### Loading data

Write a function `import_data(filename)` that imports data from a CSV file into a list of Python dictionaries. (Hint: look at the `csv` Python package and its `DictReader` class.)

### Saving data

Write a function `export_data(data, filename)` that exports the race statistics to a CSV file. (Hint: look at the `csv` Python package and its `DictWriter` class.) Should return `True` if succeeds, otherwise `False`.

### Choosing data

Write a function `clean_data(data)` that takes in a list of data points and selects the most recent one for each person. Assume no people have duplicate names.

### Print Winner

Write a function `print_winner(data)` that takes in a list of statistics (including person, total time, average velocity, and final velocity) and prints the name of the person with the shortest time.


## Message Descrambler

Pop culture is obsessed with the idea of hidden messages in audio recordings. Most notable is the idea of using [backmasking](https://en.wikipedia.org/wiki/Backmasking) to record messages backwards. Obsessions like these led to accusations of musicians including demonic messaging in their work in the twentieth century, perhaps most memorably in Led Zeppelin's [Stairway to Heaven](https://en.wikipedia.org/wiki/Stairway_to_Heaven#Claims_of_backmasking).

As it turns out, while looking through an old email account, we have stumbled upon a seemingly meaningless audio file, `mystery.wav`, which appears to just feature noise. Pretty useless. But, perhaps there's a secret message embedded within this file - we found in another email a weird CSV file `mystery.wav.csv` that appears to be related to our audio file. Upon inspecting `mystery.wav.csv`, we see that it has two fields: `From` and `To`. Maybe this file was scrambled by moving audio frames around according to the data recorded in the CSV file! Let's write a program to find out.

### Usage

Most of the usage details are handled for you in `unmix.py`. Read through that file to gain an understanding of how to check argv and call functions from `helpers.py`.

```
python unmix.py <in.wav> <in.csv> <out.wav>
```

### Background

A `wav` audio file stores sound as a series of "frames." To make the audio playback work, the file also stores the frame rate, number of frames, and a few other pieces of information so that audio players know the rate at which to play the sound data stored in binary. (It's kind of like video - frames played at a certain rate - just without pictures and with sound instead.)

In `mystery.wav.csv` the two columns of information store the location `From` which the frame at location `To` was taken. In other words, when scrambling the audio, the scrambler program saved the frame's original location to `From` and its destination to `To`. To descramble `mystery.wav`, we'll need to move frames back to their original locations.

### Loading data

Write a function `import_data(filename)` that imports data from a CSV file into a list of Python dictionaries. (Hint: look at the `csv` Python package and its `DictReader` class.) Depending on your implementation in **Smoots** you may be able to use the same function you wrote for that problem.

### Replace frames

Write a function `replace_frames(infile, reorders)` that puts frames into the right order, returning a list of binary objects. You are given the input file pointer (e.g. the `mystery.wav` pointer) and the list of reorders you collected in `import_data` (e.g. a list of dictionaries with `From` and `To` fields).

For this part of the problem, you will want to look at the documentation for the Python `wave` package and specifically on wave_read objects [here](https://docs.python.org/3/library/wave.html#wave-read-objects). (Hint: you can call these functions like this: `infile.close()`.)

### Combine bytes

Write a function `combine_bytes(reorder)` that takes a list of bytes and outputs a single binary object that combines, in order, all the elements of the list.
