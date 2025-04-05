#!/usr/bin/env python3

'''
This script troubleshoots the execution of the glade binary in the Replit environment.
'''

import os
import subprocess
import sys

def check_binary():
    print("=== CHECKING BINARY ===")
    
    # Check if file exists
    if not os.path.exists('./glade'):
        print("ERROR: 'glade' binary not found!")
        return False
    
    # Check if file is executable
    if not os.access('./glade', os.X_OK):
        print("Making binary executable...")
        os.chmod('./glade', 0o755)
    
    # Check file type
    try:
        file_type = subprocess.run(['file', './glade'], capture_output=True, text=True)
        print(f"File type: {file_type.stdout}")
        
        # Check if it's an ELF binary
        if "ELF" not in file_type.stdout:
            print("WARNING: This does not appear to be an ELF binary!")
    except Exception as e:
        print(f"Error checking file type: {e}")
    
    return True

def run_basic_test():
    print("\n=== RUNNING BASIC TEST ===")
    
    try:
        # Try running the binary with no input to see any output
        proc = subprocess.Popen(['./glade'], 
                              stdin=subprocess.PIPE, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        
        # Send minimal input
        stdout, stderr = proc.communicate(input="w\n", timeout=3)
        
        print("STDOUT:")
        print(stdout)
        
        if stderr:
            print("STDERR:")
            print(stderr)
            
        if not stdout and not stderr:
            print("WARNING: Binary produced no output. It may not be functioning correctly.")
    except subprocess.TimeoutExpired:
        print("The process timed out. It might be waiting for more input.")
    except Exception as e:
        print(f"Error running binary: {e}")

def check_environment():
    print("\n=== CHECKING ENVIRONMENT ===")
    
    # Check OS
    try:
        uname_output = subprocess.run(['uname', '-a'], capture_output=True, text=True)
        print(f"OS: {uname_output.stdout}")
    except Exception:
        print("Couldn't determine OS")
    
    # Check working directory
    print(f"Working directory: {os.getcwd()}")
    
    # Check libraries
    try:
        ldd_output = subprocess.run(['ldd', './glade'], capture_output=True, text=True)
        print("Library dependencies:")
        print(ldd_output.stdout)
    except Exception:
        print("Couldn't check library dependencies")

def try_alternative_solutions():
    print("\n=== TRYING ALTERNATIVE SOLUTIONS ===")
    
    # Some very basic solutions
    solutions = [
        "a", "s", "d", "w",
        "wasd",
        "asdw",
        "wdsa"
    ]
    
    for solution in solutions:
        print(f"Trying: {solution}")
        try:
            proc = subprocess.Popen(['./glade'], 
                                  stdin=subprocess.PIPE, 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.PIPE,
                                  text=True)
            
            stdout, stderr = proc.communicate(input=solution, timeout=3)
            
            if stdout:
                print(f"Output: {stdout}")
            if "flag" in stdout.lower():
                print("POTENTIAL FLAG FOUND!")
                
            if stderr:
                print(f"Error: {stderr}")
                
        except Exception as e:
            print(f"Error: {e}")
        
        print("-" * 30)

def try_strace():
    print("\n=== TRYING STRACE ===")
    
    try:
        # Check if strace is available
        subprocess.run(['which', 'strace'], check=True, capture_output=True)
        
        # Run with strace to see system calls
        print("Running binary with strace...")
        strace_output = subprocess.run(['strace', './glade'], 
                                     input="w\n", 
                                     text=True, 
                                     capture_output=True)
        
        print("Strace output (first 20 lines):")
        lines = strace_output.stderr.split('\n')
        for line in lines[:20]:
            print(line)
    except subprocess.CalledProcessError:
        print("strace not available")
    except Exception as e:
        print(f"Error with strace: {e}")

def suggest_next_steps():
    print("\n=== SUGGESTIONS ===")
    print("1. Try running the binary manually with: ./glade")
    print("2. Try alternative solutions from solutions.txt")
    print("3. Try copying the binary to /tmp directory:")
    print("   cp glade /tmp && cd /tmp && chmod +x glade && ./glade")
    print("4. Try another Linux environment (Docker, VM, etc.)")
    print("5. Make sure the binary is not corrupted during upload")

def main():
    print("GLADE BINARY TROUBLESHOOTER")
    print("===========================\n")
    
    # Check if binary exists and is executable
    if not check_binary():
        print("Fix the binary issues first!")
        return
    
    # Run basic test
    run_basic_test()
    
    # Check environment
    check_environment()
    
    # Try alternative solutions
    try_alternative_solutions()
    
    # Try strace if available
    try_strace()
    
    # Suggest next steps
    suggest_next_steps()

if __name__ == "__main__":
    main() 