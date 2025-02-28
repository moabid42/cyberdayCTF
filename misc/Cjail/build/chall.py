import os
import re

def is_unsafe_code(code: str) -> bool:
    patterns = [r'[{][^}]', r'[^{][}]', r';', r'#', r'%', r'\?', r'<', r'_', r'system']
    return any(re.search(pattern, code) for pattern in patterns)

def main():
    os.system("touch b.out")
    code = input("Input C code: ")
    
    if len(input()) > 55 or is_unsafe_code(code):
        quit()
    
    with open("safe.c", "w") as file:
        file.write(code)
    
    os.system("cc safe.c && ./a.out")

if __name__ == "__main__":
    main()
