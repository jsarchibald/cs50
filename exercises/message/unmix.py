import csv
import sys
import wave
import helpers

def main():
    if len(sys.argv) < 4:
        print("Usage: python unmix.py <in.wav> <in.csv> <out.wav>")
        sys.exit()
    
    with wave.open(sys.argv[1], "rb") as infile:
        # Get wave header info
        frames = infile.getnframes()
        framerate = infile.getframerate()
        channels = infile.getnchannels()
        sampwidth = infile.getsampwidth()
        comptype = infile.getcomptype()
        compname = infile.getcompname()

        # Import switch data
        reorders = helpers.import_data(sys.argv[2])

        # Loop through all frames and replace them
        reorder = helpers.replace_frames(infile, reorders)

        # Save new file
        with wave.open(sys.argv[3], "wb") as outfile:
            outfile.setparams((channels, sampwidth, framerate, frames, comptype, compname))
            outfile.writeframes(helpers.combine_bytes(reorder))
        

if __name__ == "__main__":
    main()
    