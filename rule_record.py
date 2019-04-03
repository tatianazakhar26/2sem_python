import tkinter
from heap import *

size_tk = '500x400+300+200'
def Rules():
    root_rule = tkinter.Tk()
    root_rule.title("Rules of bulls and cows")
    root_rule.geometry(size_tk)
    label_rule = tkinter.Label(root_rule, fg='black', font='arial 14', text='Быки '
            'и коровы — логическая игра, в ходе которой \nза несколько поп'
            'ыток один игрок должен определить,\n что задумал другой игрок.'
            ' в случае игры с компьютером,\n он загадывает число с n попарн'
            'о различными цифрами, \nгде число n выбирает пользователь.  По'
            'сле каждой \nпопытки задумавший игрок выставляет «оценку», \nука'
            'зывая количество угаданного без совпадения с их \nпозициями '
            '(количество «коров»)\n и полных совпадений (количество «быков»).\nПриятной игры!')
    label_rule.pack()

def Records(records):
    root_record = tkinter.Tk()
    root_record.title("Rules of bulls and cows")
    root_record.geometry(size_tk)
    label_record = tkinter.Label(root_record, fg='black', font='arial 14', text=records.__str__())
    label_record.pack()
