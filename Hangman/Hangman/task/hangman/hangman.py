import random
import string

# Write your code here
print(f'''H A N G M A N''')

ASCII_LOWERCASE_CHARS = string.ascii_lowercase
available_words = ('python', 'java', 'kotlin', 'javascript')
randomly_picked_word = random.choice(available_words)
guessed_word_progress = '-' * len(randomly_picked_word)
valid_user_input_log = []
tries = 8


def game_engine(letter):
    global guessed_word_progress
    global tries
    if len(letter) is not 1:
        print('You should print a single letter .')
        return
    if letter not in ASCII_LOWERCASE_CHARS:
        print('It is not an ASCII lowercase letter.')
        return
    if letter in valid_user_input_log:
        print('You already typed this letter')
        return
    valid_user_input_log.append(letter)
    if letter not in randomly_picked_word:
        print('No such letter in the word')
        tries -= 1
        return
    positions_of_guessed_letter = [pos for pos, char in enumerate(randomly_picked_word) if char == letter]
    guessed_word_progress_list = list(guessed_word_progress)
    for index in positions_of_guessed_letter:
        guessed_word_progress_list[index] = letter
    guessed_word_progress = ''.join(str(index) for index in guessed_word_progress_list)


while True:
    if tries <= 0:
        print('You are hanged!')
        break
    print('\n' + guessed_word_progress)
    if guessed_word_progress == randomly_picked_word:
        print('You guessed the word!')
        print('You survived!')
        break
    guessed_letter = input('Input a letter:')
    game_engine(guessed_letter)

