import re
with open('input.txt') as f:
    lines = f.readlines()

pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
do = True
total_sum = 0
for line in lines:
    all_matches = re.finditer(pattern, line)
    for match in all_matches:
        action = match.group()
        if action.startswith('don\'t()'):
            do = False
        elif action.startswith('do()'):
            do = True
        elif do and action.startswith('mul'):
            num1, num2 = map(int, re.findall(r'\d+', action))
            total_sum += num1 * num2

print(total_sum)
        