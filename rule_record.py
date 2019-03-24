from tkinter import *
def Rules():
    root_rule = Tk()
    root_rule.title("Rules of bulls and cows")
    root_rule.geometry('500x400+300+200')
    label_rule = Label(root_rule, fg='black', font='arial 14', text='Быки и коровы — логическая игра, в ходе которой \nза несколько попыток один игрок должен определить,\n что задумал другой игрок. в случае игры с компьютером,\n он загадывает число с n попарно различными цифрами, \nгде число n выбирает пользователь.  После каждой попытки \nзадумавший игрок выставляет «оценку», указывая количество\n угаданного без совпадения\ с их позициями (количество «коров»)\n и полных совпадений (количество «быков»).\nПриятной игры!')
    label_rule.pack()
def str_(heap):
    string_ = ''
    i = 1
    for (rec, name) in sorted(heap):
        string_ = string_ + '{0}.\t{1}\t{2}\n'.format(i, name, -rec)
        i += 1
    return string_
def Records(records):
    root_record = Tk()
    root_record.title("Rules of bulls and cows")
    root_record.geometry('500x400+300+200')
    rec = str_(records)
    label_record = Label(root_record, fg='black', font='arial 14', text=rec)
    label_record.pack()