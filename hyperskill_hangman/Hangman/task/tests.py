from hstest.stage_test import *
from hstest.test_case import TestCase
from hstest.check_result import accept, wrong

from random import shuffle, randint
from string import ascii_lowercase, ascii_letters, punctuation, digits


description_list = ['python', 'java', 'kotlin', 'javascript']
out_of_description = ['clojure', 'haskell', 'typescript', 'assembler']

catch = {i: 0 for i in description_list}
all_letters = ascii_letters + punctuation + digits


class CoffeeMachineTest(StageTest):
    def generate(self) -> List[TestCase]:
        tests = []

        for word in description_list + out_of_description + [ascii_lowercase]:
            for i in range(100):
                words = [w if randint(1, 100) < 95 else w + w for w in word * 50 + all_letters]
                shuffle(words)
                inputs = '\n'.join(words)
                inputs = 'play\n' + inputs + '\nexit'
                tests += [TestCase(stdin=inputs, attach=words)]

        shuffle(tests)
        return tests

    def check(self, reply: str, attach: Any) -> CheckResult:

        tries = [i.strip() for i in reply.split('\n\n') if len(i.strip())][1:]

        if len(tries) == 0:
            return wrong(
                "Seems like you didn't print the game or not separated output properly"
                "(there need to be an empty line between guessing attempts)"
            )

        full_blocks = [try_ for try_ in tries if len(try_.splitlines()) > 1]
        blocks = [block.splitlines()[0].strip() for block in full_blocks]

        for full_block, block in zip(full_blocks, blocks):
            if ' ' in block:
                return wrong(
                    'Cannot parse this block - it contains spaces '
                    'in the first line, but shouldn\'t\n\n'
                    f'{full_block}'
                )

        survived = 'You survived!'
        hanged = 'You are hanged!'

        is_survived = survived in full_blocks[-1]
        is_hanged = hanged in full_blocks[-1]

        no_such_letter = 'No such letter in the word'
        already_typed = 'You already typed this letter'
        not_ascii = 'It is not an ASCII lowercase letter'
        print_single = 'You should print a single letter'

        lengths = set(len(i) for i in blocks)

        str_lengths = []
        for i, curr_len in enumerate(lengths, 1):
            for curr_block in blocks:
                if curr_len == len(curr_block):
                    str_lengths += [f'{i}. {curr_block}']
                    break

        str_lengths = '\n'.join(str_lengths)

        if len(lengths) > 1:
            return wrong(
                f'Every line with guessed letters should be the same length as others.\n'
                f'Found lines with guessed letters:\n{str_lengths}'
            )

        correct = '-'*len(blocks[0])

        if blocks[0] != correct:
            return wrong(
                f'The first guess should only contain dashes: \n'
                f'{correct}\n'
                f'Your first guess:\n'
                f'{blocks[0]}'
            )

        wrong_count = 0
        typed_letters = set()
        inputs = ''

        if is_hanged:
            blocks += [blocks[-1]]
            full_blocks += [full_blocks[-1]]

        for letter, prev, next, prev_full, next_full in zip(
                attach, blocks[0:], blocks[1:], full_blocks[0:], full_blocks[1:]):

            # ---
            detect_not_one = len(letter) != 1

            if detect_not_one and print_single not in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is no \"{print_single}\" message, but should be'
                )
            elif not detect_not_one and print_single in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is \"{print_single}\" message, but shouldn\'t be'
                )

            if detect_not_one:
                continue

            # ---
            detect_not_ascii = letter not in ascii_lowercase

            if detect_not_ascii and not_ascii not in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is no \"{not_ascii}\" message, but should be'
                )
            elif not detect_not_ascii and not_ascii in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is \"{not_ascii}\" message, but shouldn\'t be'
                )

            if detect_not_ascii:
                continue

            inputs += '\n' + letter

            # ---
            detect_typed_letter = letter in typed_letters

            if detect_typed_letter and already_typed not in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is no \"{already_typed}\" message, but should be\n'
                    f'Input letters: {inputs}'
                )
            elif not detect_typed_letter and already_typed in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is \"{already_typed}\" message, but shouldn\'t be'
                    f'Input letters: {inputs}'
                )

            if detect_typed_letter:
                continue

            # ---
            detect_no_such_letter = (
                (letter not in prev) and
                (letter not in next) and
                (next == prev) and not detect_typed_letter
            )

            if detect_no_such_letter and no_such_letter not in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is no \"{no_such_letter}\" message, but should be'
                )
            elif not detect_no_such_letter and no_such_letter in prev_full:
                return wrong(
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}\n\n'
                    f'There is \"{no_such_letter}\" message, but shouldn\'t be'
                )

            if detect_no_such_letter:
                wrong_count += 1

            typed_letters |= {letter}

            cond1 = (
                (letter not in prev) and
                (letter in next) and
                (set(next) - set(prev) != set(letter))
            )

            cond2 = (
                (letter not in prev) and
                (letter not in next) and
                (next != prev)
            )

            cond3 = (
                (letter in prev) and
                (letter in next) and
                (next != prev)
            )

            if cond1 or cond2 or cond3:
                return wrong(
                    f'This transition is incorrect:\n'
                    f'Before: {prev}\n'
                    f'Letter: {letter}\n'
                    f'After : {next}'
                )

        if is_survived and is_hanged:
            return wrong(
                f'Looks like your output contains both \"{survived}\"'
                f' and \"{hanged}\". You should output only one of them.'
            )

        if not is_survived and not is_hanged:
            return wrong(
                f'Looks like your output doesn\'t contain neither \"{survived}\"'
                f' nor \"{hanged}\". You should output one of them.'
            )

        if is_hanged:
            if wrong_count != 8:
                return wrong(
                    f'User was hanged after {wrong_count} wrong guesses, but should after 8'
                )
            else:
                return accept()

        if is_survived:
            if wrong_count >= 8:
                return wrong(
                    f'User survived but have {wrong_count} wrong guesses. He should be hanged'
                )
            else:
                return accept()


if __name__ == '__main__':
    CoffeeMachineTest('hangman.hangman').run_tests()
