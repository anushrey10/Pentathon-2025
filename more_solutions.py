#!/usr/bin/env python3

'''
Since our first batch of solutions didn't yield the flag, let's try some more variations
with different patterns and approaches.
'''

def generate_solutions():
    # Some completely new patterns to try
    new_solutions = [
        # Shorter patterns that might be more manageable
        "wdsa",
        "dsaw",
        "wasd",
        "daswdaswdaswdasw",
        "dwdwdwdwasasasas",
        
        # Following walls in a classic maze-solving algorithm (right-hand rule)
        "dddddwwwwwaaaaaassssss",
        "dddwwwaasss",
        "ddwdwdwawawa",
        
        # Patterns with more balance between directions
        "dwswadwswadwswa",
        "dwsadwsadwsadwsa",
        
        # Simple repeating patterns
        "dddssswwwaaadddssswwwaaa",
        "ddssaawwddssaaww",
        
        # Patterns based on the maze structure
        "ddwaawddwaawddwaawd",
        "ssdwaassddwwaassdwa",
        
        # Variations on previously tried patterns with modifications
        "ddwdwwawwddssddwawssawwddssdwawssaawddssd",
        "dwawdwawdwawdwawdwawdw",
        "dwdwwawwawwddssdw",
        
        # Completely reverse patterns
        "wawdssdwawwaaswawdssdwawwaaswawdssd",
        
        # Patterns that might not seem obvious
        "dsawwadssawwadssaw",
        "wdaawdsswdaawdss",
        
        # Complete simple sequence repetitions
        "dwadwadwadwadwadwadwadwa",
        "sdwsdwsdwsdwsdwsdwsdwsdw",
        "dwasdwasdwasdwasdwasdwas",
    ]
    
    # Generate variations by slightly altering existing solutions
    variations = []
    base_patterns = [
        "dwaw", "dsaw", "dssw", "dwds", "dwsd", "dssdwa"
    ]
    
    for pattern in base_patterns:
        # Repeat the pattern different numbers of times
        for i in range(1, 6):
            variations.append(pattern * i)
            
        # Add variations with slight modifications
        variations.append(pattern.replace('w', 's'))
        variations.append(pattern.replace('a', 'd'))
        
    return new_solutions + variations

# Generate and print solutions
solutions = generate_solutions()

print("NEW QUAGMIRE SOLUTIONS TO TRY")
print("=============================")
print("Since the previous solutions didn't yield the flag, try these alternatives:\n")

for i, solution in enumerate(solutions, 1):
    print(f"{i}. {solution}")

print("\nRemember:")
print("1. These need to be run on a Linux system where the binary can execute")
print("2. The correct sequence should produce a message with the actual flag")
print("3. The flag format is likely 'flag{...}' or similar")

print("\nAlternatively: Try running the binary with a debugger to analyze its behavior")
print("You could look for sections where it compares your input with the expected path")
print("or where it generates the flag output.") 