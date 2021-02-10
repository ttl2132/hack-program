#!/usr/bin/env python

"""
Functions of Pig Latin code.
"""

import string

def translate(isinteractive, file=None):
    """
    Prints the input in Pig Latin.

    Parameters
    ----------
    isinteractive (bool):
        "file" and "input" options for program
    file (str, optional):
        File to translate. Defaults to None.
    """
    text = ""
    if isinteractive:
        print("Ellohay! Welcome to the Pig Latin translator.")
        while True:
            try:
                text = input(
                    "Enter some text to translate. Type Ctrl+C to leave the translator.\n"
                )
                translated_line = [translate_word(word) for word in text.split()]
                print(" ".join(translated_line))
            except KeyboardInterrupt:
                print("\nEbyay!")
                break
    else:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                translated_line = [translate_word(word) for word in line.split()]
                print(" ".join(translated_line))

def translate_word(word):
    """
    Returns a single word translated to Pig Latin.
    
    For simplicity sake, the characters 'y' and 'Y' are always treated as consonants.

    Parameters
    ----------
    word (str):
        The word to translate.
    """

    # Creating variables to store the prefix of the original word and the remaining characters.
    prefix = ""
    suffix = word
    punct = ""

    # Consonant rule
    while len(suffix) and not suffix[0] in "aeiouAEIOU" + string.punctuation:
        prefix = prefix + suffix[0]
        suffix = suffix[1:]

    # Removing ending punctuation
    while len(suffix) and suffix[len(suffix)-1] in string.punctuation:
        last_index = len(suffix)-1
        punct = suffix[last_index] + punct
        suffix = suffix[:last_index]
        
    return suffix + prefix + "ay" + punct

if __name__ == "__main__":
    translate(True)
    translate(False, file="../sample.txt")