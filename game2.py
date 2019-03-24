import random
def is_correct(number):
    t = True
    for i in range(len(number)):
        if number.rfind(str(number[i])) != i:
            t = False
    return t
def make_secret(n):
    s = str(random.randint(1,9))
    for i in range(n - 1):
        s = s + str(random.randint(0,9))
    while not is_correct(s):
        s = str(random.randint(1, 9))
        for i in range(n - 1):
            s = s + str(random.randint(0, 9))
    return s
def count_of_animals(secret, number):
    if not is_correct(number):
        print('It is not correct number')
        return False
    if len(secret) != len(number):
        print('It is not correct number')
        return False
    num_bulls = 0
    for i in range(len(secret)):
        if secret[i] == number[i]:
            num_bulls += 1
    num_cows = 0 - num_bulls
    for i in range(len(secret)):
        if number.find(str(secret[i])) != -1:
            num_cows += 1
    print('bulls:{}'.format(num_bulls))
    print('cows:{}'.format(num_cows))
    if num_bulls == len(secret):
        return True
    else:
        return False
def Game():
    messagebox.showinfo("Description: game", "You will be work with console")
    print('what is your name?')
    name = input()
    print('How much digits will be in numbers?')
    n = int(input())
    while n > 9:
        print("It is too big, make new")
        n = int(input())
    secret = make_secret(n)
    print('i made a number, what do you think?')
    number = input()
    iter = 1
    while not count_of_animals(secret, number):
        print('What do you think now?')
        number = input()
        iter += 1
    print('You are win in {} iterations!'.format(iter))
    return name, iter