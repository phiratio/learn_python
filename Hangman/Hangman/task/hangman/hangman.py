import random

# Write your code here
print(f'''H A N G M A N''')

available_words = ('python', 'java', 'kotlin', 'javascript')
randomly_picked_word = random.choice(available_words)
guessed_word_progress = '-' * len(randomly_picked_word)
tries = 8


def game_engine(letter):
    global guessed_word_progress
    if letter not in randomly_picked_word:
        print('No such letter in the word')
        return
    positions_of_guessed_letter = [pos for pos, char in enumerate(randomly_picked_word) if char == letter]
    guessed_word_progress_list = list(guessed_word_progress)
    for index in positions_of_guessed_letter:
        guessed_word_progress_list[index] = letter
    guessed_word_progress = ''.join(str(index) for index in guessed_word_progress_list)


while True:
    if tries <= 0:
        print('\nThanks for playing!\nWe\'ll see how well you did in the next stage')
        break
    print('\n' + guessed_word_progress)
    guessed_letter = input('Input a letter:').lower()
    game_engine(guessed_letter)
    tries -= 1

