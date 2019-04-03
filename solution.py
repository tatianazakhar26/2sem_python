import rule_record
import ungame
import tkinter
from heap import *

size_tk = '500x400+300+200'
records = Heap()
def record_():
    rule_record.Records(records)
root = tkinter.Tk()
root.title("Rules of bulls and cows")
root.geometry(size_tk)
button_game = tkinter.Button(root,text='Game',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=records.game)
button_game.pack()
button_ungame = tkinter.Button(root,text='Ungame',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=ungame.ungame)
button_ungame.pack()
button_rule = tkinter.Button(root,text='Rules',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=rule_record.Rules)
button_rule.pack()
button_rec = tkinter.Button(root,text='Records',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=record_)
button_rec.pack()
root.mainloop()
