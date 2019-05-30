print('You enter a dark room with thwo doors. Do ya go thru door 1 or door 2')

door = input('which one? > ')

if str(door) == "1":
    print('''
    There\'s a giant bear here eating a cheese cake. What do you do?
    1. Take the cake.
    2. Scream at the bear.
    ''')
    bear = input('pick > ')
    if str(bear) == "1":
        print('''
    Oopsie, bear eats ur ass
    ''')
    elif str(bear) == "2":
        print('''
    Bear screams back.. and kills you
    ''')
    else:
        print(f'''
    veri gud -> {bear} is good action
    ''')
elif str(door) == "2":
    print(f'''
You stare into the endless abyss at Cthululus retina.
1. Blueberries.
2. Yellow jacket clothespins.
3. Understanding revolvers yelling melodies
    ''')
    insanity = input('> ')
    print(insanity)
    if insanity in(['1', '2']):
        print(f'''
Your body survives powered by a mind of jello. GJ
        ''')
    else:
        print(f'The insanity rots your eyes into a pool of much. GJ')
else:
    print('GAME OVER')
