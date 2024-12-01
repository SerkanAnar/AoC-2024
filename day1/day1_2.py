
l1 = []
l2 = []
with open('input.txt', 'r') as f:

    line = f.readline()
    while line:
        val1, val2 = line.strip().split('   ')
        l1.append(int(val1))
        l2.append(int(val2))
        line = f.readline()

sum = 0
freq_dict = {}

for val in l2:
    if val in freq_dict:
        freq_dict[val] += 1
    else:
        freq_dict[val] = 1

for val in l1:
    if val in freq_dict:
        sum += val*freq_dict[val]

print(sum)