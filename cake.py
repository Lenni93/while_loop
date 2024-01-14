length = int(input())
width = int(input())
pc_cake = width * length
command = input()
while command != "STOP":
    current_pc = int(command)
    pc_cake -= current_pc
    if pc_cake < 0:
        break
    command = input()
# command is looking for stop if is not stop will continue if is 0 will be done
if pc_cake < 0:
    print(f"No more cake left! You need {abs(pc_cake)} pieces more.")
else:
    print(f"{pc_cake} pieces are left.")
