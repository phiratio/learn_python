from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, i'm the %s script." % (user_name, script))
print('do you liek me %s?' % user_name)
likes = input(prompt)
print('wer du u liv %s?' % user_name)
lives = input(prompt)
print('wat komputar do u hevb %s?' % user_name)
computer = input(prompt)

print('''
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
''' % (likes, lives, computer))
