import argparse

from autobleep import AutoBleep

parser = argparse.ArgumentParser(
    prog="AutoBleep",
    description="AutoBleep parses an audio or video file and automatically bleeps the swear words",
    epilog="Text at the bottom of help",
)

parser.add_argument("-i", "--input", dest="input", help="the video file to bleep")

parser.add_argument(
    "-o", "--output", dest="output", help="the destination output file path"
)

args = parser.parse_args()

autobleep = AutoBleep(args.input)
