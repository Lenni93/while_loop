import sys
num = input()
min_num = sys.maxsize
total = 0

while num != 'Stop':
    total = int(num)

    if total < min_num:
        min_num = total

    num = input()

print(min_num)
