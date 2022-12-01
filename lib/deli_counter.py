def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for index, el in enumerate(katz_deli):
            message += f' {index + 1}. {katz_deli[index]}'
        print(message)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]
