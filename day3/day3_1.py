import re
with open('input.txt') as f:
    lines = f.readlines()

total_sum = 0
for line in lines:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for match in matches:
        nums = re.findall(r'\d+,\d+', match)
        nums = nums[0].split(',')
        num1, num2 = int(nums[0]), int(nums[1])
        total_sum += num1 * num2

print(total_sum)