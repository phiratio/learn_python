def unpack(input_tuple):
    unpacked = tuple()

    for item in input_tuple:
        if isinstance(item, tuple):
            for x in item:
                unpacked += (x,)
        else:
            unpacked += (item,)

    return unpacked


hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'))

z = unpack(hobbies_Adam)
print(z)