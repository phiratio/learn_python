import random

# Write your code here
print(f'''H A N G M A N''')

available_words = ('python', 'java', 'kotlin', 'javascript')
randomly_picked_word = random.choice(available_words)
guessed_word_progress = '-' * len(randomly_picked_word)
tries = 8


def game_engine(letter):
    global guessed_word_progress
    global tries
    if letter not in randomly_picked_word:
        print('No such letter in the word')
        tries -= 1
        return
    if letter in guessed_word_progress:
        print('No improvements')
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
    guessed_letter = input('Input a letter:').lower()
    game_engine(guessed_letter)

