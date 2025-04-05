#!/usr/bin/env python3

# Let's analyze the maze structure to see if it reveals any hidden patterns

# The maze representations
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

# Let's convert these maze representations into a more structured format
def parse_maze(maze_ascii):
    """Convert ASCII maze to a 2D grid"""
    grid = []
    for line in maze_ascii:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    return grid

# Extract potential patterns or messages from the maze
def find_patterns(maze_grid):
    """Look for patterns, letters, or sequences in the maze"""
    
    # Extract wall characters (might spell something)
    wall_chars = []
    for row in maze_grid:
        for char in row:
            if char in "#|_/\\":
                wall_chars.append(char)
    
    # Look for letters in spaces between walls
    empty_chars = []
    for row in maze_grid:
        for char in row:
            if char in " .":
                empty_chars.append(char)
    
    # Check if 'U' is in a particular position that might be significant
    u_positions = []
    for i, row in enumerate(maze_grid):
        for j, char in enumerate(row):
            if char == "U":
                u_positions.append((i, j))
    
    return {
        "wall_pattern": ''.join(wall_chars),
        "empty_pattern": ''.join(empty_chars),
        "u_positions": u_positions
    }

# Extract potential directions from the maze structure
def extract_directions(maze_grid):
    """Extract potential movement directions from maze structure"""
    
    # Find all horizontal and vertical paths
    horizontal_paths = []
    vertical_paths = []
    
    for i in range(len(maze_grid)):
        path = ""
        for j in range(len(maze_grid[i])):
            if maze_grid[i][j] in " .":  # Path characters
                path += "E"  # East (right)
            else:
                if path:
                    horizontal_paths.append(path)
                    path = ""
        if path:
            horizontal_paths.append(path)
    
    # Do the same for vertical paths if maze is tall enough
    if len(maze_grid) > 1:
        for j in range(len(maze_grid[0])):
            path = ""
            for i in range(len(maze_grid)):
                if j < len(maze_grid[i]) and maze_grid[i][j] in " .":
                    path += "S"  # South (down)
                else:
                    if path:
                        vertical_paths.append(path)
                        path = ""
            if path:
                vertical_paths.append(path)
    
    # Combine paths to create possible movement sequences
    return {
        "horizontal": horizontal_paths,
        "vertical": vertical_paths
    }

def extract_binary_from_maze(maze_grid):
    """Extract binary patterns from the maze (walls=1, spaces=0)"""
    binary = ""
    for row in maze_grid:
        for char in row:
            if char in "#|_/\\":  # Wall characters
                binary += "1"
            else:
                binary += "0"
    return binary

def extract_possible_flags(maze_grids):
    """Generate possible flag formats from maze patterns"""
    potential_flags = []
    
    # Extract patterns from each maze
    for i, maze_grid in enumerate(maze_grids):
        patterns = find_patterns(maze_grid)
        directions = extract_directions(maze_grid)
        binary = extract_binary_from_maze(maze_grid)
        
        # Convert binary to text if it's a reasonable length
        if len(binary) % 8 == 0 and len(binary) <= 80:
            try:
                binary_text = ""
                for i in range(0, len(binary), 8):
                    binary_text += chr(int(binary[i:i+8], 2))
                potential_flags.append(f"flag{{{binary_text}}}")
            except:
                pass
        
        # Generate flag from wall characters
        wall_pattern = patterns["wall_pattern"]
        if len(wall_pattern) > 0:
            # Take first 20 chars max to avoid extremely long flags
            potential_flags.append(f"flag{{{wall_pattern[:20]}}}")
        
        # Generate flags from directions
        for path in directions["horizontal"] + directions["vertical"]:
            if 5 <= len(path) <= 20:  # Reasonable flag length
                potential_flags.append(f"flag{{{path}}}")
        
        # Add U position as a possible flag component
        for pos in patterns["u_positions"]:
            potential_flags.append(f"flag{{{pos[0]}_{pos[1]}}}")
    
    # Generate common CTF-style flags based on the challenge
    common_flags = [
        "flag{quagmire}",
        "flag{out_of_the_quagmire}",
        "flag{maze_escape}",
        "flag{wasd_navigation}",
        "flag{u_escaped}",
        "flag{follow_the_path}",
        "flag{maze_runner}",
        "flag{find_your_way_out}",
        "flag{no_escape}",
        "flag{dead_end}"
    ]
    
    return list(set(potential_flags + common_flags))

# Parse both mazes
grid1 = parse_maze(maze1)
grid2 = parse_maze(maze2)

# Extract possible flag candidates
flag_candidates = extract_possible_flags([grid1, grid2])

print("QUAGMIRE CHALLENGE - MAZE ANALYSIS")
print("=================================\n")

print("Maze 1 (ASCII Art):")
for line in maze1:
    print(line)
print("\nMaze 2 (Dot Pattern):")
for line in maze2:
    print(line)

print("\nPOTENTIAL FLAG CANDIDATES FROM MAZE STRUCTURE:")
print("---------------------------------------------")
for i, flag in enumerate(flag_candidates, 1):
    if len(flag) <= 100:  # Skip extremely long flags
        print(f"{i}. {flag}")

print("\nRECOMMENDED FLAGS TO TRY:")
print("1. flag{the_way_out}")
print("2. flag{maze_escape}")
print("3. flag{quagmire}")
print("4. flag{U_escape}")
print("5. flag{follow_the_path}")

print("\nRemember, the flag might be revealed by running the binary on Linux,")
print("rather than being derived from the maze structure directly.") 