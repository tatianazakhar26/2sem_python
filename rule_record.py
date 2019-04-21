import tkinter
import heap
import constants

def Rules():
    const = constants.Const()
    root_rule = tkinter.Tk()
    root_rule.title(const.title + ": rules")
    root_rule.geometry(const.size_tk)
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
    const = constants.Const()
    root_record = tkinter.Tk()
    root_record.title(const.title +  ": records")
    root_record.geometry(const.size_tk)
    label_record = tkinter.Label(root_record, fg='black', font='arial 14', text=records.__str__())
    label_record.pack()
