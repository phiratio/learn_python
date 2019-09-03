import random

# Write your code here
print(f'''H A N G M A N
The game will be available soon.''')

available_words = ('python', 'java', 'kotlin', 'javascript')
guessed_word = input('Guess the word: ')
guessed_word = guessed_word.lower()
print('You survived!') if guessed_word == random.choice(available_words) else print('You are hanged!')
