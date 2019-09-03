import random

# Write your code here
print(f'''H A N G M A N
The game will be available soon.''')

available_words = ('python', 'java', 'kotlin', 'javascript')
randomly_picked_word = random.choice(available_words)


def hint_formatter(word):
    return word[0:3] + '-' * (len(word[3:]))


guessed_word = input(f'''Guess the word {hint_formatter(randomly_picked_word)}: ''')
guessed_word = guessed_word.lower()
print('You survived!') if guessed_word == randomly_picked_word else print('You are hanged!')
