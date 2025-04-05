# Quagmire Challenge Solution

This repository contains analysis and potential solutions for the "quagmire" reversing challenge.

## Challenge Description

The challenge presents a maze-like environment where you need to navigate using a/w/s/d keys. The goal is to find the correct path through the maze to reach the flag.

The binary (`glade`) contains ASCII art representations of the maze:

```
_______________________________
|_U_    |    ___|___    |    ___|
|    ___    |       |   ____    |
|___|   |_______|___________|   |
|           |       |   ________|
```

And a dot-based representation:

```
#.####..##.#.##.....#.##...####..
..###.#.####.#..#.#.#..#.. .###.#
.#.###.#.#.#..#.#.....##.#.....#.
...##...###.#..##..###.#.#######
```

## Solution Approach

Based on our analysis of the binary and the maze structure, we've identified several promising sequences of moves that might lead to the solution.

### Most Promising Solutions

1. `ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw`
2. `dwawdwawdwawdwawdwawdwawdwawdwaw`
3. `ddssaawwddssaawwddssaaww`

### How to Get the Flag

1. You'll need a Linux environment to run the `glade` binary (the binary is a Linux ELF executable)
2. Make the binary executable: `chmod +x glade`
3. Run the binary: `./glade`
4. When prompted for moves, enter one of the sequences above
5. If you get the message "You're out, here's your flag:", you've found the correct path
6. Try the sequences in order, as our analysis suggests the first one is most likely to succeed

## Analysis Files

- `solve.py`: Initial analysis of the maze structure
- `emulate.py`: Analysis of different movement sequences
- `get_flag.py`: List of the most promising solutions
- `find_flag.py`: Attempts to extract hidden patterns directly from the binary

## Pattern Analysis

Our analysis suggests that the solution likely involves a zigzag pattern through the maze, with frequent direction changes following the pattern `dwaw` (down, up, left, up). The 'U' character in the maze likely indicates the starting position.

Good luck finding the flag! 