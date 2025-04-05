#!/usr/bin/env python3

'''
This script will try all the movement sequences on the glade binary.
Upload this script and the glade binary to Replit to run it.
'''

import subprocess
import time
import os

# All potential solutions
solutions = [
    # Most promising solutions first
    "ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw",
    "dwawdwawdwawdwawdwawdwawdwawdwaw",
    "ddwdwawwddssdwawssaawwddssdwawssaawwddssdwa",
    "ddssaawwddssaawwddssaaww", 
    "ddssddssddsswwaawwaawwaaddsswwaassddwwaa",
    "dwadwadwadwadwadwa",
    "wasd",
    "dsaw",
    "daswdaswdaswdasw",
    "dwdwdwdwasasasas",
    "dddddwwwwwaaaaaassssss",
    "dddwwwaasss",
    "ddwdwdwawawa"
]

def try_solution(solution):
    """Try a solution on the glade binary"""
    print(f"Trying solution: {solution}")
    
    try:
        # Make sure the file is executable
        if not os.access('./glade', os.X_OK):
            print("Making glade executable...")
            os.chmod('./glade', 0o755)
        
        # Run the binary with the solution as input
        proc = subprocess.Popen(['./glade'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               text=True)
        
        # Send the solution and get the output
        stdout, stderr = proc.communicate(input=solution, timeout=5)
        
        # Print the output
        print("OUTPUT:")
        print(stdout)
        
        # Check if the flag message is in the output
        if "You're out, here's your flag:" in stdout:
            print("\n🎯 SUCCESS! FOUND THE FLAG! 🎯")
            
            # Extract the flag using a simple pattern match
            flag_start = stdout.find("You're out, here's your flag:") + len("You're out, here's your flag:")
            flag_text = stdout[flag_start:].strip()
            
            print(f"FLAG: {flag_text}")
            return True
        else:
            print("This solution didn't work\n")
            return False
            
    except subprocess.TimeoutExpired:
        print("The process timed out (took too long)")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    print("QUAGMIRE CHALLENGE - SOLUTION TESTER")
    print("====================================")
    print(f"Will try {len(solutions)} potential solutions\n")
    
    # Check if the glade file exists
    if not os.path.exists('./glade'):
        print("Error: 'glade' binary not found in the current directory")
        print("Make sure you've uploaded the 'glade' file to Replit")
        return
    
    success = False
    for i, solution in enumerate(solutions, 1):
        print(f"Attempt {i}/{len(solutions)}")
        success = try_solution(solution)
        if success:
            print(f"\nSuccessful solution: {solution}")
            break
        
        # Small delay between attempts
        time.sleep(1)
    
    if not success:
        print("\nNone of the solutions worked.")
        print("You might need to try some of the other solutions manually.")
        
if __name__ == "__main__":
    main() 