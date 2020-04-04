# Code Listing #3

"""

Code testing the 'eval' function for security holes

"""

# 03-test_eval.py
import sys
import os


def run_code(string):
    """ Evaluate the passed string as code """

    try:
        eval(string, {})
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    run_code(sys.argv[1])

    # pwn
    # python2 03-test_eval.py "__import__('os').system('ls -a')"