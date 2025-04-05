#!/usr/bin/env python3

'''
This script analyzes the binary for any hidden information that might 
contain or reveal the actual flag.
'''

import re
import subprocess
import os

# Base64 and hex patterns to look for
base64_pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
hex_pattern = r'[0-9a-fA-F]{16,}'
flag_pattern = r'flag{[^}]+}'

def find_strings_in_binary():
    """Use strings command to extract readable text from the binary"""
    try:
        result = subprocess.run(['strings', 'glade'], capture_output=True, text=True)
        strings_output = result.stdout.split('\n')
        
        # Extract potentially interesting strings
        interesting = []
        for line in strings_output:
            # Skip very short strings
            if len(line) < 5:
                continue
                
            # Look for flag pattern directly
            if re.search(flag_pattern, line, re.IGNORECASE):
                interesting.append(('POTENTIAL FLAG', line))
                
            # Look for base64-encoded data
            elif re.search(base64_pattern, line):
                interesting.append(('BASE64', line))
                
            # Look for hex data
            elif re.search(hex_pattern, line):
                interesting.append(('HEX', line))
                
            # Look for messages related to flags
            elif 'flag' in line.lower() or 'out' in line.lower() or 'escape' in line.lower():
                interesting.append(('KEYWORD', line))
        
        return interesting
    except Exception as e:
        return [('ERROR', f"Error running strings: {e}")]

def analyze_binary_data():
    """Analyze binary data chunks for patterns"""
    try:
        # Use xxd for hex dump
        result = subprocess.run(['xxd', 'glade'], capture_output=True, text=True)
        xxd_output = result.stdout.split('\n')
        
        # Look for patterns in the hex data
        patterns = []
        for line in xxd_output:
            # Look for flag-like patterns in hex
            if 'flag' in line.lower():
                patterns.append(('FLAG HEX', line))
                
            # Look for ASCII text in hex
            ascii_part = line[48:] if len(line) > 48 else ""
            if re.search(r'[a-zA-Z0-9]{4,}', ascii_part):
                patterns.append(('ASCII TEXT', line))
        
        return patterns
    except Exception as e:
        return [('ERROR', f"Error analyzing binary: {e}")]

def extract_flag_from_output():
    """Look for flag in output messages from the binary"""
    try:
        # We can't run the binary directly on macOS, but we can check for output messages
        strings_result = subprocess.run(['strings', 'glade'], capture_output=True, text=True)
        output_lines = strings_result.stdout.split('\n')
        
        # Look for output messages that might contain the flag
        flag_messages = []
        for i, line in enumerate(output_lines):
            if "flag" in line.lower() or "out" in line.lower():
                # Get this line and the next few lines
                context = '\n'.join(output_lines[i:i+5]) if i+5 < len(output_lines) else '\n'.join(output_lines[i:])
                flag_messages.append(context)
        
        return flag_messages
    except Exception as e:
        return [f"Error extracting flag: {e}"]

def check_executable_strings():
    """Check the binary for hard-coded strings like the flag"""
    try:
        # More thorough search for strings
        result = subprocess.run(['strings', '-a', '-t', 'x', 'glade'], capture_output=True, text=True)
        output = result.stdout.split('\n')
        
        # Look for interesting strings with their offsets
        interesting = []
        for line in output:
            if len(line) > 10 and ('flag' in line.lower() or '{' in line or '}' in line):
                interesting.append(line)
        
        return interesting
    except Exception as e:
        return [f"Error checking executable: {e}"]

def check_file_metadata():
    """Check file metadata for clues"""
    try:
        # Get file information
        file_info = subprocess.run(['file', 'glade'], capture_output=True, text=True)
        file_info_output = file_info.stdout
        
        # Get file size
        file_size = os.path.getsize('glade')
        
        return [
            f"File info: {file_info_output}",
            f"File size: {file_size} bytes"
        ]
    except Exception as e:
        return [f"Error checking metadata: {e}"]

print("QUAGMIRE CHALLENGE - BINARY ANALYSIS")
print("===================================\n")

print("SEARCHING FOR READABLE STRINGS IN BINARY:")
print("-----------------------------------------")
strings = find_strings_in_binary()
for type, text in strings:
    print(f"{type}: {text}")

print("\nANALYZING BINARY DATA PATTERNS:")
print("-------------------------------")
patterns = analyze_binary_data()
for type, pattern in patterns[:20]:  # Limit to first 20 to avoid overwhelming output
    print(f"{type}: {pattern}")

print("\nLOOKING FOR FLAG IN OUTPUT MESSAGES:")
print("-----------------------------------")
flag_messages = extract_flag_from_output()
for message in flag_messages:
    print(message)
    print("-----")

print("\nCHECKING FOR HARDCODED STRINGS:")
print("------------------------------")
hardcoded = check_executable_strings()
for string in hardcoded[:20]:  # Limit to first 20
    print(string)

print("\nFILE METADATA:")
print("-------------")
metadata = check_file_metadata()
for info in metadata:
    print(info)

print("\nPOTENTIAL FLAGS TO TRY:")
print("---------------------")
print("flag{quagmire}")
print("flag{glade}")
print("flag{maze_escape}")
print("flag{the_way_out}")
print("flag{find_your_way}")
print("flag{out_of_the_quagmire}")
print("flag{follow_the_path}")
print("flag{pathfinder}")
print("flag{navigation}")
print("flag{not_a_dead_end}")

print("\nRemember: The ultimate solution likely requires running the binary on Linux.")
print("The flag is probably generated or displayed by the program when you successfully")
print("navigate through the maze using the right sequence of moves.") 