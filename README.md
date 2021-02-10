# Pig Latin Translator

This package takes a file of text and tranlates it into Pig Latin, or provides an interactive input area for quick, on-the-go translations.

## Installation
```pip install -e .```

## Usage
```bash
usage: piglatin [-h] [-f FILE] [-i]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  the file to be translated
  -i, --input           interactive translator option in terminal
```

## Sample Code
- ```piglatin --help```
- ```piglatin -i```
- Assuming you are in the hack-program directory: ```piglatin -f sample.txt```