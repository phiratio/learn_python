from sys import exit


def gold_room():
    print('Dis rum is ful of geld! How much y u take?')

    next = input(">  ")
    try:
        how_much = int(next)
    except ValueError:
        dead("man learn to type number")

    if how_much < 50:
        print('not greedy - gg')
        exit(0)
    else:
        dead("you greedy bastard!")


def bear_room():
    print(f'''
    There is a bear here.
    The bear has a bunch of honey
    The fat bear is in front of another door
    How are you going to move the bear
    ''')
    bear_moved = False

    while True:
        next = input(">  ")
        if next == "take honey":
            dead('bear kilz u')
        elif next == "taunt bear" and not bear_moved:
            print('the bear has moved from the door. You can go through it now')
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead('bear is pissed and eatz u')
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print('i got no idea what that means')


def cthulhu_room():
    print('''
    Here you see the great evil Cthulhu
    He, it whatever stares at you and you go insane
    Do you flee for your life or eat your head?
    ''')
    next = input(">   ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(f'{why}, GJ BRUH')
    exit(0)


def start():
    print('''
    You are in a dark room
    There is a door to your right and left
    WHich one do you take
    ''')
    next = input(">   ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
