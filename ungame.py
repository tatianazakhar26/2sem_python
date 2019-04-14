import random
import time
from tkinter import messagebox

def is_correct(number: int) -> bool:
    if len(number) == 1:
        return True
    if number[0] == number[1]:
        return False
    return len(set(number)) == len(number)

def first(n):
    if n == 1:
        return 1
    fst = 10
    for i in range(2, n):
        fst = 10 * fst + i
    return fst

def last(n):
    lst = 0
    for i in range(9, 9 - n, -1):
        lst = 10 * lst + i
    return lst

def gen(bulls, cows, number, *sol):
    for secret in sol:
        num_bulls = 0
        for j in range(len(secret)):
            if secret[j] == number[j]:
                num_bulls += 1
        num_cows = 0 - num_bulls
        for j in range(len(secret)):
            if number.find(str(secret[j])) != -1:
                num_cows += 1
        if bulls == num_bulls and cows == num_cows:
            yield secret

def ungame():
    messagebox.showinfo("Description: ungame", "You will be work with console")
    print('How much digits will be in number?')
    n = int(input())
    while n > 9 or n <= 0:
        print("It is too big, make new")
        n = int(input())
    sol = []
    if n == 1:
        sol = [str(i) for i in range(0, 10)]
    else:
        sol = [str(i) for i in range(first(n), last(n)) if is_correct(str(i))]
    bulls = 0
    cows = 0
    while bulls != n and len(sol) > 0:
        number = sol[random.randint(0, len(sol) - 1)]
        print(number)
        print('bulls:')
        bulls = int(input())
        print('cows:')
        cows = int(input())
        sol = [i for i in gen(bulls, cows, number, *sol)]
    if len(sol) == 0 :
        print("Error")
    else:
        print('Your secret is {}'.format(sol[0]))
