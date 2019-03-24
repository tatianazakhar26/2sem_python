import game2
import rule_record
import ungame
from tkinter import *
import heapq
root=Tk()
root.title("Bulls and cows")
records = []
def game_():
    name, record = game2.Game()
    heapq.heappush(records, (-record, name))
    if len(records) > 10:
        heapq.heappop(records)
def record_():
    rule_record.Records(records)
root.geometry('500x400+300+200')
button_game = Button(root,text='Game',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=game_)
button_game.pack()
button_ungame = Button(root,text='Ungame',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=ungame.ungame)
button_ungame.pack()
button_rule = Button(root,text='Rules',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=rule_record.Rules)
button_rule.pack()
button_rec = Button(root,text='Records',width=25,height=3,fg='black',bg='#7FFFD4',font='arial 14', command=record_)
button_rec.pack()
root.mainloop()

