import argparse
import os
import re
import sys

parser = argparse.ArgumentParser(description="wc clone")
parser.add_argument('-c', action="store_true")
parser.add_argument('-l', action="store_true")
parser.add_argument('-w', action="store_true")
parser.add_argument('-m', action="store_true")
parser.add_argument('filename', nargs='?')


def readFile(filename):
    file = open(filename, "r")
    return file


def remove_multiple_whitespaces(input_string):
    # from ChatGPT
    # Use a regular expression to replace multiple whitespaces with a single whitespace
    output_string = re.sub(r'\s+', ' ', input_string.strip())
    return output_string


def getBytes(line):
    return len(line.encode('utf-8'))


if __name__ == '__main__':
    args = parser.parse_args()
    filename = args.filename
    if (not args.c and not args.l and not args.w and not args.m):
        args.c = args.l = args.w = True
    try:
        file = None
        if filename:
            file = readFile(filename)
        else:
            file = sys.stdin
        nb_bytes = 0
        nb_lines = 0
        nb_words = 0
        nb_characters = 0
        for line in file:
            nb_lines += 1
            nb_bytes += getBytes(line+("\n" if filename else ""))
            nb_characters += len(line)+(1 if filename else 0)
            line = remove_multiple_whitespaces(line)
            if line == '':
                continue
            nb_words += len(list(line.split(' ')))

        if args.l:
            print(nb_lines, end=" ")

        if args.w:
            print(nb_words, end=" ")

        if args.m:
            print(nb_characters, end=" ")

        if args.c:
            print(nb_bytes, end=" ")
        if (filename):
            print(filename)
        else:
            print()
        if file is not None:
            file.close()
    except Exception as e:
        print(e)
