import sys

# The maze representation
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

# Binary data pattern found in the executable
# These could represent the correct path or a map of valid/invalid moves
binary_pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Potential moves sequences to try
# Based on observed maze structure
sequences = [
    "dddddwwwwassssddddwwwwaaa",
    "dddddssssaaaawwwwddddsss",
    "aaaawwwwddddsssswwwwaaaa",
    "ssssaaaawwwwddddsssaaaaw",
    "ddssddssddsswwaawwaawwaaddsswwaassddwwaa",
    "ddssaawwddssaawwddssaaww",
    "ddddsssswwwwaaaa",
    "aaaawwwwddddsssss",
    "wawdwawdwawdwawd",
    "wdwawdwawdwawdwa",
    "ddddssssaaaawwww",
    "ssssaaaawwwwdddd",
    "ddssaawwddssaaww",
    "aawwddssaawwddss",
    # Analyzing maze pattern visually suggests this could be a solution
    "ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw"
]

print("Possible solution paths for the quagmire maze:")
for i, seq in enumerate(sequences):
    print(f"{i+1}. {seq}")

print("\nVisual maze representation:")
for line in maze1:
    print(line)
print("\nSecond maze representation:")
for line in maze2:
    print(line)

print("\nBinary pattern found in executable (could be the maze map):")
for row in binary_pattern:
    print(''.join(str(bit) for bit in row))

print("\nAnalysis:")
print("1. The maze appears to be a grid where you navigate using a/w/s/d keys.")
print("2. The binary patterns might represent valid/invalid paths or walls.")
print("3. Try the sequences above in the actual challenge executable.")
print("4. Based on the maze visualization, sequence #15 is my best guess.")
print("   It follows a zigzag pattern through the maze avoiding dead ends.") 