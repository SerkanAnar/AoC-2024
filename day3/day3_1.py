import re
with open('input.txt') as f:
    lines = f.readlines()

total_sum = 0
for line in lines:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for match in matches:
        nums = re.findall(r'\d+,\d+', match)
        num1, num2 = map(int, re.findall(r'\d+', nums[0]))
        total_sum += num1 * num2

print(total_sum)