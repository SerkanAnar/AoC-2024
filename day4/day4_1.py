with open('input.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

total_sum = 0
# i, j grid indices
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'X':
            if i >= 3:
                if lines[i-1][j] + lines[i-2][j] + lines[i-3][j] == 'MAS':
                    total_sum += 1
            if i >= 3 and len(lines[0])-j >= 4:
                if lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3] == "MAS":
                    total_sum += 1
            if len(lines[0])-j >= 4:
                if lines[i][j+1] + lines[i][j+2] + lines[i][j+3] == 'MAS':
                    total_sum += 1
            if len(lines) - i >= 4 and len(lines[0])-j >= 4:
                if lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == 'MAS':
                    total_sum += 1
            if len(lines) - i >= 4:
                if lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == 'MAS':
                    total_sum += 1
            if len(lines) - i >= 4 and j >= 3:
                if lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] == 'MAS':
                    total_sum += 1
            if j >= 3:
                if lines[i][j-1] + lines[i][j-2] + lines[i][j-3] == 'MAS':
                    total_sum += 1
            if i >= 3 and j >= 3:
                if lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3] == 'MAS':
                    total_sum += 1

print(total_sum)