from sys import argv
from os.path import exists

self, copyFrom, copyTo = argv
print('Copying from %s to %s' % (copyFrom, copyTo))
dataToCopy = open(copyFrom, 'r').read()
print('the input file is %r bytes long' % dataToCopy)
print('Does the output file exists? %r' % exists(copyTo))
input('Ready, hit enter to continue, Ctrl+C to abort')

out_file = open(copyTo, 'w')
out_file.write(dataToCopy)
print('done')
out_file.close()
