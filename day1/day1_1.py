l1 = []
l2 = []
with open('input.txt', 'r') as f:

    line = f.readline()
    while line:
        val1, val2 = line.strip().split('   ')
        l1.append(int(val1))
        l2.append(int(val2))
        line = f.readline()

l1.sort()
l2.sort()

sum = 0

for i in range(len(l1)):
    sum += abs(l1[i]-l2[i])

print(sum)