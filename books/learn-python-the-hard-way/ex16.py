from sys import argv

script, filename = argv
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input('?')
print('Opening the file...')
fileToManipulate = open(filename, 'w+')  # 1
print('File contains:')
print(fileToManipulate.read())  # why not working i've set +flag.. :TODO
print('Truncating the file. BB data')
fileToManipulate.truncate()  # 2   not needed because w flag does it
print('now you\'ll be asken for 3 lines')
l1 = input('GIVE A LINE  > ')
l2 = input('GIVE A LINE  > ')
l3 = input('GIVE A LINE  > ')
nl = '\n'
print('Now we\'ll write these to da file')
lines = l1+nl+l2+nl+l3+nl
fileToManipulate.write(lines)  # 3
print('Nice let\'s see wat we got')
fileToManipulate.close()  # 4
print(open(filename).read())
