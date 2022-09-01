items = [['apple', 1], ['banana', 2], ['coffee', 3], ['donut', 4], ['eggs', 5]]

cart = list()

for item in items:
    item_name = item[0]
    item_cost = item[1]
    user_input_accepted = False
    total_cost = 0
    while user_input_accepted == False:
        add_item = input(
            f'Would you like an {item_name} for ${item_cost}? (y or n)')
        if add_item.lower() == 'y' or add_item.lower() == 'yes':
            cart.append(item)
            total_cost += item_cost
            user_input_accepted = True
        elif add_item.lower() == 'n' or add_item.lower() == 'no':
            user_input_accepted = True
        else:
            print(
                f'Your input: {add_item} is not accepted. Please input y or n.'
            )

print('Here is your cart:')
print(cart)

user_input_accepted = False
while user_input_accepted == False:
    remove_items = input(f'Would you like to remove any items? (y or n)')
    if remove_items.lower() == 'y' or remove_items.lower() == 'yes':
        remove_items = True
        user_input_accepted = True
    elif remove_items.lower() == 'n' or remove_items.lower() == 'no':
        remove_items = False
        user_input_accepted = True
    else:
        print(
            f'Your input: {remove_items} is not accepted. Please input y or n.'
        )

while remove_items:
    user_input_accepted = False
    while user_input_accepted == False:
        item_to_remove = input(
            'Please input the name of the item you\'d like to remove')
        for item in cart:
            if item_to_remove == item[0]:
                cart.remove(item)
                user_input_accepted = True
                break
        if user_input_accepted == False:
            print(f'Your input: {item_to_remove} is not found.')
    remove_items = input(f'Would you like to remove any more items? (y or n)')
    if remove_items.lower() == 'y' or remove_items.lower() == 'yes':
        remove_items = True
    elif remove_items.lower() == 'n' or remove_items.lower() == 'no':
        remove_items = False

print(cart)


