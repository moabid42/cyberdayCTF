import base64
import os

def obfuscate_python(program, key):
    obfuscated_program = "".join(chr(ord(c) ^ key) for c in program)
    
    encoded = base64.b64encode(obfuscated_program.encode()).decode()
    
    obfuscated_code = '__FOLLOW_MALWAREKID___FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__ = ""\n'
    for i in range(0, len(encoded), 10):
        chunk = encoded[i:i+10]
        hex_chunk = ''.join(['\\x{:02x}'.format(ord(c)) for c in chunk])
        obfuscated_code += '__FOLLOW_MALWAREKID___FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__ += "{}"\n'.format(hex_chunk)
    
    obfuscated_code += 'exec("".join(chr(ord(c) ^ {}) for c in __import__("base64").b64decode(__FOLLOW_MALWAREKID___FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__).decode()))'.format(key)
    return obfuscated_code


def main():
    try:
        python_code = input("Enter your python code to obfuscate (leave empty for program path): ")
        if not python_code:
            program_path = input("Enter your python program path: ")
            while not os.path.exists(program_path):
                print("Invalid path. Please try again.")
                program_path = input("Enter your python program path: ")
            with open(program_path, 'r') as file:
                python_code = file.read()
        
        obfuscated_program_name = input("Enter your obfuscated program name (default obfuscate.py): ")
        if not obfuscated_program_name:
            obfuscated_program_name = "obfuscate.py"
        
        key = 0x42
        
        obfuscated_code = obfuscate_python(python_code, key)
        
        with open(obfuscated_program_name, 'w') as file:
            file.write(obfuscated_code)
        
        print(f"Obfuscated program has been saved as {obfuscated_program_name}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting...")

if __name__ == "__main__":
    main()
