needed_money = float(input()) 
current_money = float(input())

spending_counter = 0
spend_money_counter = 0
total_days = 0
money = False
while current_money < needed_money:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == 'spend':
        spending_counter += 1
        if spending_counter == 5:
            money = True
            break
        current_money -= current_sum
        if current_money < 0:
            current_money = 0
    elif action == 'save':
        current_money += current_sum
        spending_counter = 0

if money:
    print(f"You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")