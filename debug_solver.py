#!/usr/bin/env python3

'''
Debug version of the solver script that shows more output and tests the binary more thoroughly.
'''

import subprocess
import time
import os
import sys

def test_binary_works():
    """Test if the binary runs at all"""
    print("Testing if binary runs...")
    
    try:
        # Check file type
        file_cmd = subprocess.run(['file', './glade'], capture_output=True, text=True)
        print(f"File type: {file_cmd.stdout}")
        
        # Make executable
        os.chmod('./glade', 0o755)
        
        # Run a simple test
        proc = subprocess.Popen(['./glade'], 
                              stdin=subprocess.PIPE, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        
        # Wait a moment to see if it starts
        time.sleep(1)
        
        # Check if process is still running
        if proc.poll() is None:
            print("Binary appears to be running!")
            # Send 'q' to quit
            proc.communicate(input='q', timeout=1)
        else:
            stdout, stderr = proc.communicate()
            print(f"Binary exited immediately with code {proc.returncode}")
            if stdout:
                print(f"STDOUT: {stdout}")
            if stderr:
                print(f"STDERR: {stderr}")
            
            return False
    except Exception as e:
        print(f"Error testing binary: {e}")
        return False
    
    return True

def run_with_input(input_text):
    """Run the binary with the given input and show detailed output"""
    print(f"Running with input: {input_text}")
    
    try:
        # Run the process with detailed monitoring
        proc = subprocess.Popen(['./glade'], 
                              stdin=subprocess.PIPE, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE)
        
        # Write each character with a delay to mimic typing
        for char in input_text:
            proc.stdin.write(char.encode())
            proc.stdin.flush()
            time.sleep(0.1)
        
        # Add newline at the end
        proc.stdin.write(b'\n')
        proc.stdin.flush()
        
        # Wait a moment to collect output
        time.sleep(1)
        
        # Read output if available
        output = b''
        while proc.poll() is None:
            # Read available output without blocking
            if proc.stdout.readable():
                chunk = proc.stdout.read1(1024)
                if chunk:
                    output += chunk
                else:
                    break
        
        # Get any remaining output
        stdout, stderr = proc.communicate(timeout=2)
        output += stdout if stdout else b''
        
        # Convert to string and display
        output_str = output.decode('utf-8', errors='replace')
        print("OUTPUT:")
        print(output_str)
        
        # Check for flag
        if "flag" in output_str.lower():
            print("POTENTIAL FLAG MENTION FOUND!")
        
        # Show error if any
        if stderr:
            print("STDERR:")
            print(stderr.decode('utf-8', errors='replace'))
        
        return output_str
    except Exception as e:
        print(f"Error: {e}")
        return ""

def try_simpler_solutions():
    """Try a series of very simple inputs"""
    print("\n=== TRYING SIMPLE INPUTS ===")
    
    simple_inputs = [
        "w", "a", "s", "d",  # Single moves
        "wasd",             # Basic sequence
        "ww", "aa", "ss", "dd",  # Double moves
        "wwaassdd",         # Simple pattern
        "wwwwaaaassssdddd"  # Extended pattern
    ]
    
    for input_text in simple_inputs:
        print(f"\nTrying: {input_text}")
        output = run_with_input(input_text)
        print("-" * 40)
        time.sleep(1)

def try_main_solutions():
    """Try the main solutions we think might work"""
    print("\n=== TRYING MAIN SOLUTIONS ===")
    
    solutions = [
        "ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw",
        "dwawdwawdwawdwawdwawdwawdwawdwaw",
        "ddssaawwddssaawwddssaaww"
    ]
    
    for solution in solutions:
        print(f"\nTrying solution: {solution}")
        output = run_with_input(solution)
        print("-" * 40)
        time.sleep(1)

def try_alternative_location():
    """Try running the binary from /tmp directory"""
    print("\n=== TRYING FROM /TMP DIRECTORY ===")
    
    try:
        # Copy to /tmp
        subprocess.run(['cp', './glade', '/tmp/'], check=True)
        subprocess.run(['chmod', '+x', '/tmp/glade'], check=True)
        
        # Try running from there with a simple input
        proc = subprocess.Popen(['cd', '/tmp', '&&', './glade'], 
                             shell=True,
                             stdin=subprocess.PIPE, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE,
                             text=True)
        
        stdout, stderr = proc.communicate(input="wasd\n", timeout=3)
        
        print("OUTPUT FROM /TMP:")
        print(stdout)
        
        if stderr:
            print("STDERR:")
            print(stderr)
            
    except Exception as e:
        print(f"Error trying alternative location: {e}")

def main():
    print("GLADE BINARY DEBUG TESTER")
    print("========================\n")
    
    # Check if file exists
    if not os.path.exists('./glade'):
        print("ERROR: glade binary not found! Make sure you've uploaded it.")
        return
    
    # Test if binary works at all
    if not test_binary_works():
        print("\nWARNING: The binary doesn't appear to be working correctly.")
        print("This might be due to issues with the Replit environment or the binary itself.")
        print("Let's try some tests anyway...\n")
    
    # Try simple solutions
    try_simpler_solutions()
    
    # Try main solutions
    try_main_solutions()
    
    # Try alternative location
    try_alternative_location()
    
    print("\n=== SUGGESTIONS ===")
    print("1. Try running the binary manually: ./glade")
    print("2. If no output appears, the binary might not work in this environment")
    print("3. Consider using Docker or a Linux VM instead")
    print("4. Make sure the binary file wasn't corrupted during upload")
    print("5. You can download these files and run them in another Linux environment:")
    print("   - glade: The original binary")
    print("   - replit_solver.py: Our automated solution tester")
    print("   - debug_solver.py: This debug script")

if __name__ == "__main__":
    main() 