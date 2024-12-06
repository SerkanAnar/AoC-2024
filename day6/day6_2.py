import copy

def get_initial_pos(lines):
    for x in range(len(lines)):
        for y in range(len(lines[0])): # Assuming that each line has same length
            if lines[x][y] == '^':
                return x, y

def get_obstacle_positions(lines, initial_x, initial_y):
    obstacle_positions = []
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if x == initial_x and y == initial_y:
                continue
            obstacle_positions.append((x, y))
    return obstacle_positions

# Flipped x and y ... 
def detect_loop(lines, dirs, new_dirs, x, y):
    current_dir = '^'
    visited = set()
    while True:
        if (x, y, current_dir) in visited:
            return True
        visited.add((x, y, current_dir))
        dir_x, dir_y = dirs[current_dir]
        next_x, next_y = x + dir_x, y + dir_y
        if next_x >= len(lines) or next_x < 0 or next_y < 0 or next_y >= len(lines[0]):
            return False
        next_char = lines[next_x][next_y]
        if next_char == '#' or next_char == 'O':
            current_dir = new_dirs[current_dir]
        else:
            x, y = next_x, next_y

with open('input.txt') as f:
    lines = f.readlines()
lines = [list(line.strip()) for line in lines]

initial_x, initial_y = get_initial_pos(lines)
dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
new_dirs = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

obstacle_positions = get_obstacle_positions(lines, initial_x, initial_y)

total_sum = 0

for x, y in obstacle_positions:
    temp_lines = copy.deepcopy(lines)
    temp_lines[x][y] = 'O'
    if detect_loop(temp_lines, dirs, new_dirs, initial_x, initial_y):
        total_sum += 1

print(total_sum)