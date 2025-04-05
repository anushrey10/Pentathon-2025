#!/usr/bin/env python3

'''
This script attempts to find hidden patterns in the binary that might
directly reveal the flag or the solution path.
'''

import re
import subprocess
import binascii

def extract_strings_from_binary(binary_path):
    try:
        result = subprocess.run(['strings', binary_path], 
                              capture_output=True, text=True)
        return result.stdout.split('\n')
    except:
        print(f"Error: Could not run 'strings' on {binary_path}")
        return []

def find_suspicious_patterns(strings_list):
    suspicious = []
    
    # Look for flag format patterns
    flag_patterns = [
        r'flag{.*}', r'pent{.*}', r'quag{.*}', r'PENT{.*}',
        r'[a-zA-Z0-9]{32}', r'[a-zA-Z0-9-_]{24}'
    ]
    
    for s in strings_list:
        # Skip very short strings
        if len(s) < 8:
            continue
            
        # Check for flag-like patterns
        for pattern in flag_patterns:
            if re.search(pattern, s):
                suspicious.append(("Possible flag", s))
                
        # Check for base64-encoded data
        if re.match(r'^[A-Za-z0-9+/]+={0,2}$', s) and len(s) > 20:
            suspicious.append(("Possible base64", s))
            
        # Check for hidden messages
        if 'flag' in s.lower() or 'quag' in s.lower() or 'maze' in s.lower() or 'solution' in s.lower():
            suspicious.append(("Keyword found", s))
            
    return suspicious

def extract_binary_patterns(binary_path):
    try:
        # Try to extract sections that look like movement patterns
        cmd = f"dd if={binary_path} bs=1 skip=8672 count=1000 2>/dev/null | xxd -g 1"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # Look for repeating patterns
        lines = result.stdout.strip().split('\n')
        
        # Extract the 0/1 patterns
        pattern = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 9:  # Skip header line
                for i in range(2, min(10, len(parts))):
                    if parts[i] == '01000000':
                        pattern.append('1')
                    elif parts[i] == '00000000':
                        pattern.append('0')
        
        # Convert to potental movement directions
        moves = []
        direction_map = {'00': 'w', '01': 'd', '10': 'a', '11': 's'}
        
        for i in range(0, len(pattern)-1, 2):
            if i+1 < len(pattern):
                pair = pattern[i] + pattern[i+1]
                if pair in direction_map:
                    moves.append(direction_map[pair])
                    
        return ''.join(moves)
    except:
        return "Failed to extract binary patterns"

print("QUAGMIRE CHALLENGE - Direct Flag Search")
print("=======================================")

# Extract strings from binary
strings = extract_strings_from_binary('./glade')
if strings:
    print(f"Extracted {len(strings)} strings from binary")
    
    # Find suspicious patterns
    suspicious = find_suspicious_patterns(strings)
    if suspicious:
        print("\nInteresting patterns found:")
        for pattern_type, content in suspicious:
            print(f"{pattern_type}: {content}")
    else:
        print("No suspicious patterns found in strings")

# Try to extract movement pattern from binary data
binary_pattern = extract_binary_patterns('./glade')
print("\nPossible encoded movement pattern:")
print(binary_pattern)

print("\nRecommended solution sequences:")
print("1. ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw")
print("2. dwawdwawdwawdwawdwawdwawdwawdwaw")
print("3. ddssaawwddssaawwddssaaww")

print("\nWhen running the binary, enter these sequences at the prompt to find the flag.") 