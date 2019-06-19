phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
sliceTo = int(len(phrase) / 2)
first_half = phrase[:sliceTo]
print(first_half)
