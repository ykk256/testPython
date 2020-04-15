def collatz(number):
    if int(number) % 2 == 0:
        return int(number) / 2
    else:
        return 3 * int(number) + 1

input_number = input()
while 1:
    print(input_number)
    try:
        input_number = collatz(input_number)
    except ValueError:
        print("ValueError")
        break
    if input_number == 1:
        print('break')
        break
