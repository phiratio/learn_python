the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f'{number}')

for x in change:
    print(f'{x}')

elements = []

for i in range(0, 7):
    print(f'Adding {i} to the list')
    elements.append(i)

print(f'this is elements now -> {elements}')
