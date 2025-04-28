list_numbers = [] 
while True:
    list_numbers.append(int(input('Enter a number: ')))
    continue_input = str(input('Do you want to continue? [Y/N] '))
    while continue_input not in 'YyNn':
        continue_input = str(input('ERROR! Do you want to continue? [Y/N] '))
    if continue_input in 'Nn':
        break

print(f'{len(list_numbers)} numbers were added to the list.'.title())

list_numbers.sort()  
print(f'The list in ascending order is: {list_numbers}'.title())

list_numbers.reverse() 
print(f'The list in reverse order is: {list_numbers}'.title())

if 5 in list_numbers:
    print('The number 5 is present in the list.')
else:
    print('The number 5 is not present in the list.')
