import sys

print("Welcome to RoBo!\nBy Langdon Staab 2019-2023; Original idea by Edison Wang 2019-2021")


def help2():
    pass


def sudoku():
    if sys.argv[2].isdigit():
        pass
    else:
        pass


def encrypt():
    pass


def decrypt():
    pass


def morse():
    pass


def credits():
    pass


def about():
    print('''\nRobo was created by Edison Wang and Langdon Staab when they were in grade 7.
It was our first coding project and our first adventure into the world of Python.
The first program was Cal, a command line calculator(with limited functionality in hindsight).
Our next program was root, a square root calculator built off the concept of the broken
Processing.JS one on hatchcoding.com.
P.S. The greatest python book of all time is \x1B[3mPython Crash Course\x1B[0m by Eric Matthes\n''')


'''def ():
    pass
def ():
    pass'''

print(sys.argv)
if len(sys.argv) > 1:
    if sys.argv[1] == "help":
        help2()
    elif sys.argv[1] == "sudoku":
        sudoku()
    elif sys.argv[1] == "decrypt":
        decrypt()
    elif sys.argv[1] == "encrypt":
        encrypt()
    elif sys.argv[1] == "morse":
        morse()
    elif sys.argv[1] == "credits":
        credits()
    elif sys.argv[1] == "about":
        about()
    '''
    elif args[] == "":
        pass
    elif args[] == "":
        pass
    elif args[] == "":
        pass
    elif args[] == "":
        pass
    elif args[] == "":
        pass'''
else:
    help2()
