goal_reached = 0
difference_distance = 0
walking_counter = 0
# calculate the distance and compared with goal
goal = 10000

while walking_counter < goal:
    end_walk = input()
    if end_walk == 'Going home':
        last_step = int(input())
        walking_counter += last_step
        break

    current_step = int(end_walk)
    walking_counter += current_step
difference_distance = abs(walking_counter - goal)
if walking_counter >= goal:
    print("Goal reached! Good job!")
    print(f'{difference_distance} steps over the goal!')
else:
    print(f'{difference_distance} more steps to reach goal.')
