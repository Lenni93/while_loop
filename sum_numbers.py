num = int(input())

diff = 0

while True:
    number = int(input())
    diff += number
    if diff >= num:
        print(diff)
        break
