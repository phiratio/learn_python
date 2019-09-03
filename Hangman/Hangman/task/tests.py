from hstest.stage_test import *
from hstest.test_case import TestCase
from hstest.check_result import accept, wrong

from random import shuffle


description_list = ['python', 'java', 'kotlin', 'javascript']
out_of_description = ['clojure', 'haskell', 'typescript', 'assembler']

catch = {i: 0 for i in description_list}


class CoffeeMachineTest(StageTest):
    def generate(self) -> List[TestCase]:
        tests = []

        for word in description_list + out_of_description:
            for i in range(100):
                tests += [TestCase(stdin=word, attach=word)]

        shuffle(tests)

        word = 'last'
        tests += [TestCase(stdin=word, attach=word)]
        return tests

    def check(self, reply: str, attach: Any) -> CheckResult:

        survived = 'You survived!'
        hanged = 'You are hanged!'

        is_survived = survived in reply
        is_hanged = hanged in reply

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

        if attach in out_of_description:
            if is_survived:
                return wrong(
                    f'Input contains a word out of the '
                    f'list form the description but the '
                    f'program output \"{survived}\"'
                )
            else:
                return accept()

        elif attach in description_list:

            if is_survived:
                hidden_attach = attach[:3] + '-'*len(attach[3:])
                if hidden_attach not in reply:
                    return wrong(
                        f'Program guessed the word \"{attach}\" '
                        f'and should output clue \"{hidden_attach}\" '
                        f'but this line is not in the output'
                    )

            catch[attach] += is_survived
            return accept()

        else:
            if any(v == 0 for v in catch.values()):
                return wrong(
                    "Looks like your program is not using "
                    "all of the words to guess from the list in description"
                )
            else:
                return accept()


if __name__ == '__main__':
    CoffeeMachineTest('hangman.hangman').run_tests()
