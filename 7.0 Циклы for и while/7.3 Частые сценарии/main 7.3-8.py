n = int(input())

total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i
    else:
        total = total - i
print(total)
