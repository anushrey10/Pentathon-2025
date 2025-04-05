#!/usr/bin/env python3

'''
This script will automatically try all the potential solutions against the glade binary.
NOTE: This script needs to be run on a Linux system, as the binary is an ELF executable.

Usage:
1. Place this script in the same directory as the 'glade' binary
2. Make both files executable: chmod +x glade run_all_solutions.py
3. Run: ./run_all_solutions.py
'''

import subprocess
import time

# All potential solutions from most likely to least likely
solutions = [
    # Most promising solutions
    "ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw",
    "dwawdwawdwawdwawdwawdwawdwawdwaw",
    "ddwdwawwddssdwawssaawwddssdwawssaawwddssdwa",
    "ddssaawwddssaawwddssaaww",
    
    # Other possible solutions
    "ddssddssddsswwaawwaawwaaddsswwaassddwwaa",
    "ddwddsswwaaasddsswwaassddsswwaa",
    "dddddwwwwassssddddwwwwaaa",
    "aaaawwwwddddsssswwwwaaaa",
    "ssssaaaawwwwddddsssaaaaw",
    "dwadwadwadwadwadwa",
    "dddddssssaaaawwwwddddsss",
    
    # Variations on the zigzag pattern
    "ddwwaasdwwaasdwwaas",
    "ddwawddwawddwawd",
    "wawdwawdwawdwawd",
    "wdwawdwawdwawdwa",
    "dwdadwdadwda",
    "wawawawawa",
    "ddddwwwwaaaasssss"
]

def try_solution(solution):
    print(f"\nTrying solution: {solution}")
    
    try:
        # Check if the 'glade' binary exists and is executable
        import os
        if not os.path.exists('./glade'):
            print("Error: 'glade' binary not found in the current directory")
            return
        
        if not os.access('./glade', os.X_OK):
            print("Making 'glade' executable...")
            os.chmod('./glade', 0o755)
        
        # Run the binary and provide the solution as input
        proc = subprocess.Popen(['./glade'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               text=True)
        
        # Send the solution and get the output
        output, _ = proc.communicate(input=solution)
        
        # Check if the flag message is in the output
        if "You're out, here's your flag:" in output:
            print("\n!!!! SUCCESS !!!!")
            print("Found the flag!")
            print(output)
            return True
        else:
            print("This solution did not work")
            return False
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    print("QUAGMIRE CHALLENGE - SOLUTION TESTER")
    print("====================================")
    print(f"Will try {len(solutions)} potential solutions\n")
    
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}/{len(solutions)}")
        success = try_solution(solution)
        if success:
            print(f"\nSuccessful solution: {solution}")
            break
        # Small delay between attempts
        time.sleep(0.5)
    
    if not success:
        print("\nNone of the solutions worked.")
        print("You might need to try more variations or analyze the binary further.")
        
if __name__ == "__main__":
    main() 