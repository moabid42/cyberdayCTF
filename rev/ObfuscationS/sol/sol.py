import base64

def deobfuscate_python(obfuscated_code, key):
    # Step 1: Extract all chunks assigned to the variable
    var_name = '__FOLLOW_MALWAREKID___FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__FOLLOW_MALWAREKID__'
    chunks = []
    lines = obfuscated_code.split('\n')
    for line in lines:
        if var_name + ' += "' in line:
            # Extract the string literal without the quotes
            chunk = line.split(' += "')[1].rstrip('"')
            chunks.append(chunk)
    
    # Step 2: Reconstruct the base64-encoded data
    # Combine all chunks and remove '\\x' prefixes
    hex_string = ''.join(chunk.replace('\\x', '') for chunk in chunks)
    # Convert hex string to bytes
    base64_data = bytes.fromhex(hex_string)
    
    # Step 3: Decode the base64 data
    decoded_data = base64.b64decode(base64_data)
    
    # Step 4: XOR-decipher the obfuscated program
    # XOR each byte with the key
    original_bytes = bytes(b ^ key for b in decoded_data)
    # Convert bytes to string
    original_program = original_bytes.decode('utf-8')
    
    return original_program

obfuscated_code = open('../dist/obfuscate.py', 'r').read()
key = 0x42 
original_code = deobfuscate_python(obfuscated_code, key)
print(original_code)
