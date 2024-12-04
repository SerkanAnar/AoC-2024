with open('input.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

total_sum = 0
# i, j grid indices
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'A':
            if i >= 1 and len(lines) - i >= 2 and j >= 1 and len(lines[0]) - j >= 2:
                if ((lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M') \
                    or (lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S')) \
                        and ((lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M') \
                             or (lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S')):
                    total_sum += 1
print(total_sum)
