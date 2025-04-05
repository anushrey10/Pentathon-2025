#!/usr/bin/env python3

# Simple emulator to try different paths through the maze
# We'll implement a basic maze navigation system based on our understanding

import re

# Define the maze (based on visualization from binary)
maze1 = [
    "_______________________________",
    "|_U_    |    ___|___    |    ___|",
    "|    ___    |       |   ____    |",
    "|___|   |_______|___________|   |",
    "|           |       |   ________|"
]

maze2 = [
    "#.####..##.#.##.....#.##...####..",
    "..###.#.####.#..#.#.#..#.. .###.#",
    ".#.###.#.#.#..#.#.....##.#.....#.",
    "...##...###.#..##..###.#.#######"
]

def try_sequence(sequence):
    print(f"Trying sequence: {sequence}")
    # In a real scenario, this would interact with the binary
    # Here we'll just print the sequence and analyze it
    
    # Analyze the sequence characteristics
    counts = {'a': 0, 'w': 0, 's': 0, 'd': 0}
    for char in sequence:
        if char in counts:
            counts[char] += 1
    
    print(f"Move counts: {counts}")
    
    # Look for patterns in the sequence
    pattern_analysis = []
    current_char = None
    current_count = 0
    
    for char in sequence:
        if char != current_char:
            if current_char:
                pattern_analysis.append(f"{current_char}x{current_count}")
            current_char = char
            current_count = 1
        else:
            current_count += 1
    
    if current_char:
        pattern_analysis.append(f"{current_char}x{current_count}")
    
    print(f"Pattern: {''.join(pattern_analysis)}")
    
    # Check if the sequence matches known patterns from the binary
    # For example, if we find a pattern that appears in the binary data
    if re.search(r'w.*d.*w.*a', sequence):
        print("* This sequence contains alternating direction changes (promising)")
    
    if len(sequence) >= 30:
        print("* Longer sequences have more potential to reach the goal")
    
    # In a real situation, we'd try this sequence with the binary
    print()

# Sequences to try (from our previous analysis)
sequences = [
    # Simple patterns first
    "dddddwwwwassssddddwwwwaaa",
    "dddddssssaaaawwwwddddsss",
    "aaaawwwwddddsssswwwwaaaa",
    "ssssaaaawwwwddddsssaaaaw",
    # More complex patterns that follow the maze structure
    "ddssddssddsswwaawwaawwaaddsswwaassddwwaa",
    "ddssaawwddssaawwddssaaww",
    # The following is our best guess based on binary patterns and maze analysis
    "ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw",
    # Variations of the best guess
    "ddwdwawwddssdwawssaawwddssdwawssaawwddssdwa",
    "dwawdwawdwawdwawdwawdwawdwawdwaw",
    # Attempt with more zigzag pattern following maze walls
    "ddwddsswwaaasddsswwaassddsswwaa",
    # Try repeating smaller patterns
    "dwadwadwadwadwadwa"
]

print("Maze Challenge Emulator\n")
print("Visual maze representation:")
for line in maze1:
    print(line)
print("\nDot maze representation:")
for line in maze2:
    print(line)
print("\n")

for seq in sequences:
    try_sequence(seq)

print("Best guess: ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw")
print("Try using this sequence in the actual binary to get the flag.")
print("\nRemember: The 'U' character likely indicates your starting position in the maze.") 