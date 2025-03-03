# Solution

Use the sol.py script to remove the first layer of obfuscation. Afterwards, either use Simba to solve the symbolic equation and see that it's just xor, or directly bruteforce the key from the expected, knowing that the first few bytes are 42HN{ (Don't forget mod 127)
