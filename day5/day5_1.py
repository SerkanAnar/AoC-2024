def create_dict(lines):
    my_dict = {}
    line = lines[0]
    i = 0
    while line != '':
        key, value = list(map(int, line.split('|')))
        if key not in my_dict:
            my_dict[key] = [value]
        else:
            l = my_dict[key]
            l.append(value)
            my_dict[key] = l
        i += 1
        line = lines[i]
    return my_dict, i

def is_correct_order(line, my_dict):
    for i in range(len(line)-1):
        first = line[i]
        for c in range(i+1, len(line)):
            next_number = line[c]
            if next_number not in my_dict.get(first, []):
                return False
    return True

with open('smallinput.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
my_dict, end = create_dict(lines)
total_sum = 0

lines = lines[end+1:]

for line in lines:
    line = list(map(int, line.split(',')))
    if is_correct_order(line, my_dict):
        total_sum += line[len(line) // 2]

print(total_sum)