print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanatio\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jarss = jelly_beans / 1000
    cratess = jarss / 100
    return jelly_beans, jarss, cratess


start_point = 10000
beans, jars, crates = secret_formula(start_point)
print(f'With a starting point of: {start_point}" "We\'d have {beans} beans, {jars} jars, and {crates} crates.')
start_point = start_point / 10
print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
