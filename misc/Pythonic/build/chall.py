#!/usr/local/bin/python

import re

illegal_pattern = re.compile(r'[^!-~]|[+;%{]|[1-9]')

def load_contrabands(file_path="words.txt"):
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f]

def check_illegal_characters(cmd):
    return bool(illegal_pattern.search(cmd))

def contains_contraband(cmd, contrabands):
    lower_cmd = cmd.lower()
    return any(word in lower_cmd for word in contrabands)

def process_command(cmd):
    try:
        print(eval(cmd, {"__builtins__": None}))
    except Exception:
        pass

def main():
    print("Welcome to your jail cell, if you are done, write 'q' or 'Q'!")
    while True:
        try:
            cmd = input("> ")
            contrabands = load_contrabands()
            if contains_contraband(cmd, contrabands) or check_illegal_characters(cmd):
                print("Yeet!")
            else:
                process_command(cmd)

            if cmd.strip().lower() == "q":
                print("Enough Yeet!")
                break
        except Exception:
            print("Yeeten't!")

if __name__ == "__main__":
    main()
