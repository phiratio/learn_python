def print_two(*args):  # :TODO *args are for funcs and argv for inputs
    arg1, arg2 = args
    print('arg1: %r, arg2: %r' % (arg1, arg2))


def print_two_again(arg1, arg2):
    print('arg1: %r, arg2: %r' % (arg1, arg2))


print_two("zdr", "zdr")
print_two_again("zdr", "zdr")
