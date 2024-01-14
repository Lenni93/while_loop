total = 0

while True:
    text = input()
    if text == "NoMoreMoney":
        break

    current_deposit_sum = float(text)

    if current_deposit_sum >= 0:
        total += current_deposit_sum
        print(f'Increase: {current_deposit_sum:.2f}')

    else:
        print('Invalid operation!')
        break

print(f'Total: {total:.2f}')

