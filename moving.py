width = int(input())
length = int(input())
height = int(input())
room_size = width * length * height
action = input()
while action != 'Done':
    current_size = int(action)
    room_size -= current_size
    if room_size < 0:
        break
    action = input()
if room_size < 0:
    print(f"No more free space! You need {abs(room_size)} Cubic meters more.")
else:
    print(f"{room_size} Cubic meters left.")





# Потребителят въвежда следните данни на отделни редове:
# 1. Широчина на свободното пространство - цяло число;
# 2. Дължина на свободното пространство - цяло число;
# 3. Височина на свободното пространство - цяло число