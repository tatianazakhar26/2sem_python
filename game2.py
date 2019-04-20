import random
import tkinter
import constants

def is_correct(number):
    if len(number) == 1:
        return True
    if number[0] == number[1]:
        return False
    return len(set(number)) == len(number)

def make_secret(n):
    const = constants.Const()
    s = str(random.randint(1, const.max_size))
    for i in range(n - 1):
        s = s + str(random.randint(0,const.max_size))
    while not is_correct(s):
        s = str(random.randint(1, const.max_size))
        for i in range(n - 1):
            s = s + str(random.randint(0, const.max_size))
    return s

def count_of_animals(secret, number: str):
    const = constants.Const()
    if not is_correct(number):
        raise Exception('It is not correct number')
    if len(secret) != len(number):
        raise Exception('It is not correct number')
    try:
        int(number)
    except:
        raise Exception('It is not correct number')
    num_bulls = sum([1 for i in range(len(secret)) if secret[i] == number[i] ])
    num_cows = sum([1 for d in secret if number.find(d) != -1]) - num_bulls
    print('bulls:{}'.format(num_bulls))
    print('cows:{}'.format(num_cows))
    return num_bulls == len(secret)

class Game():
    def __init__(self):
        const = constants.Const()
        tkinter.messagebox.showinfo("Description: game", "You will be work with console")
        print('what is your name?')
        self.name = input()
        print('How much digits will be in numbers?')
        n = int(input())
        while n > const.max_size:
            print("It is too big, make new")
            n = int(input())
        self.secret = make_secret(n)

    def go(self):
        print('i made a number, what do you think?')
        number = input()
        self.attempt = 1
        while not count_of_animals(self.secret, number):
            print('What do you think now?')
            number = input()
            self.attempt += 1
        print('You are win in {} iterations!'.format(self.attempt))
