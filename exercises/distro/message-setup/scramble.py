import csv
import random
import sys
import wave


def combine_bytes(reorder):
    """Combine list of bytes into one binary sequence"""
    o = b''
    for r in reorder:
        o += r
    return o


def scramble(infile, outfile):
    destinations = list()
    frames = infile.getnframes()
    newfile = [None] * frames

    newpos = list(range(frames))

    random.shuffle(newpos)

    for i in range(frames):
        print(f"{i + 1} of {frames}", end="\r")
        destinations.append(newpos[i])
        infile.setpos(i)
        newfile[newpos[i]] = infile.readframes(1)
    
    dicts = list()
    for i, n in enumerate(destinations):
        dicts.append({"Original": i, "Scrambled": n})

    with open(outfile, "w", newline="") as f:
        dw = csv.DictWriter(f, ["Original", "Scrambled"])

        dw.writeheader()
        dw.writerows(dicts)

    return combine_bytes(newfile)
    

def main():
    if len(sys.argv) < 4:
        print("Usage: python mix.py <in.wav> <out.csv> <out.wav>")
        sys.exit()
    
    with wave.open(sys.argv[1], "rb") as infile:
        # Get wave header info
        frames = infile.getnframes()
        framerate = infile.getframerate()
        channels = infile.getnchannels()
        sampwidth = infile.getsampwidth()
        comptype = infile.getcomptype()
        compname = infile.getcompname()

        # Scramble wave file
        output = scramble(infile, sys.argv[2])

        # Save new file
        with wave.open(sys.argv[3], "wb") as outfile:
            outfile.setparams((channels, sampwidth, framerate, frames, comptype, compname))
            outfile.writeframes(output)
        

if __name__ == "__main__":
    main()
    
