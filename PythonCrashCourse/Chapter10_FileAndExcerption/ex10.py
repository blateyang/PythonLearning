# ---------------
# Author: blateyang
# Date: 2018/3/7
# ---------------
"""Exercises of chapter 10 in PythonCrashCourse"""


def ex10_1():
    """read data from file"""
    # mode 1: read file directly
    with open('learning_python.txt') as f:
        print('first time print:')
        print(f.read())  # f object can only be read for one time

    # mode 2: read one line a time
    print('second time print:')
    with open('learning_python.txt') as f:
        for line in f:
            print(line.rstrip())

    # mode 3: store file content in a list
    with open('learning_python.txt') as f:
        python_notes = f.readlines()
    print('third time print:')
    for note in python_notes:
        print(note.rstrip())


# write file
def ex10_3():
    """write user name to file"""
    name = input('Please input your name: ')
    with open('guest.txt', 'w') as f:
        f.write(name)


def ex10_4():
    """record the situation of log in"""
    while 1:
        name = input("Please input your name(input 'q' to quit):")
        if name == 'quit':
            break
        print('Hello, '+name)
        with open('guest_book.txt', 'a') as f:
            f.write(name+' has visit.\n')


# catch exception
def ex10_6():
    """execute add operation and can deal with wrong input"""
    input_hint = "Please input two num(split by space, input 'q' to quit):"
    while True:
        user_input = input(input_hint).split(' ')
        if user_input[0] == 'q':
            break
        try:
            # convert str to int
            num1 = int(user_input[0])
            num2 = int(user_input[1])
        except ValueError:
            print('Your input include non-num, please try again.')
        else:
            print('The sum of two num is: '+str(num1+num2))


def ex10_10():
    """Count ordinary word"""
    files = ['little_princess.txt']
    for item in files:
        try:
            with open(item) as f:
                book = f.read()
                word_count = book.lower().count('the')
        except FileNotFoundError:
            print("Can't find file "+ item)
        else:
            print('There are '+str(word_count) + " 'the' in "+item)

# ex10_11
import json


def store_favorite_num():
    """store favorite number that user input"""
    num = input('Please input your favorite number: ')
    city = input('Please input cities you want to visit(split with comma):')
    city_list = city.split(',')
    info = {'num': num, 'city_list': city_list}
    with open('favorite_num.json', 'w') as f:
        json.dump(info, f)


def print_favorite_num():
    """read json file and print stored favorite number"""
    try:
        with open('favorite_num.json') as f:
            info = json.load(f)
    except FileNotFoundError:
        print('The file does not exist')
    else:
        print("I know your favorite number! It's "+ info['num'])
        print("I know the cities you want to visit1 They are:")
        for city in info['city_list']:
            print(city, end=' ')
        print()


def favorite_num():
    """store favorite number and read it from to print"""
    num = input('Please input your favorite number: ')
    with open('favorite_num.json', 'w') as f:
        json.dump(num, f)
    try:
        with open('favorite_num.json') as f:
            num = json.load(f)
    except FileNotFoundError:
        print('The file does not exist')
    else:
        print("I know your favorite number! It's "+ num)

if __name__ == '__main__':
    # ex10_3()
    # ex10_4()
    # ex10_6()
    # ex10_10()
    store_favorite_num()
    print_favorite_num()
    # favorite_num()