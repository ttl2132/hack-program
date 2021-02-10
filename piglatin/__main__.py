#!/usr/bin/env python

"""
Command line argparser for darwinday
"""

import argparse
from piglatin import translate

def parse_arguments():
    """
    Parses CLI arguments using argparse
    """

    # init argparse class object
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--file",
        help="the file to be translated"
    )

    parser.add_argument(
        "-i",
        "--input",
        action="store_true",
        help="interactive translator option in terminal"
    )

    # return arg dict-like object containing user arguments
    args = parser.parse_args()

    if args.file and args.input:
        raise SystemExit(
            "cannot enter both --file and --input at the same time"
        )
    return args

def run_program():
    "runs the command line program"
    # get CLI arguments
    args = parse_arguments()
    if args.file:
        translate(False, file=args.file)
    elif args.input:
        translate(True)
    else:
        print("Default mode (interactive) started")
        translate(True)