def check_ordering(line):
    return all(line[i] > line[i+1] for i in range(len(line)-1)) or all(line[i] < line[i+1] for i in range(len(line)-1))

def is_safe(line):
    for i in range(len(line) - 1):
        difference = abs(line[i] - line[i + 1])
        if difference < 1 or difference > 3:
            return False
    return True

with open('input.txt') as f:
    lines = f.readlines()

lines = [list(map(int, s.split())) for s in lines]
ctr = 0
for line in lines:
    if check_ordering(line):
        if (is_safe(line)):
            ctr += 1

print(ctr)