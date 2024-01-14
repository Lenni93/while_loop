import sys
num = input()
max_num = -sys.maxsize
total = 0

while num != 'Stop':
    total = int(num)

    if total > max_num:
        max_num = total

    num = input()

print(max_num)
