def get_initial_pos(lines):
    for x in range(len(lines)):
        for y in range(len(lines[0])): # Assuming that each line has same length
            if lines[x][y] == '^':
                return x, y

with open('input.txt') as f:
    lines = f.readlines()
lines = [list(line.strip()) for line in lines]

x, y = get_initial_pos(lines)
dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
new_dirs = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

current_dir = '^'
while True: # Flipped x and y ... 
    lines[x][y] = "X"
    dir_x, dir_y = dirs[current_dir]
    next_x, next_y = x + dir_x, y + dir_y
    if next_x >= len(lines) or next_x < 0 or next_y < 0 or next_y >= len(lines[0]):
        break
    next_char = lines[next_x][next_y]
    if next_char == '#':
        current_dir = new_dirs[current_dir]
    else:
        x, y = next_x, next_y

total_sum = sum(1 for row in lines for char in row if char == 'X')
print(total_sum)