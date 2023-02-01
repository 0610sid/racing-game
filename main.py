import turtle
import tkinter as tk
import random
from players import*
from tracks import*
from data import*
import sqlite3

createtable()
window = tk.Tk()
window.title("SIDs and SRUs PROJECT")
window.configure(background='#BAABDA')
window.attributes('-fullscreen',False)

name = tk.Label(window, text="RACING GAME", bg="#BAABDA", font=("Comic Sans MS",15, "bold") , width=30, height=3)
name.pack(side="top")

canvas = tk.Canvas(window ,width=1400, height=430)
canvas.pack()
 
screen = turtle.TurtleScreen(canvas)
makeTracks(canvas)
screen.bgcolor("#FFF8F3")
p1 = createTurtlePlayer('red',-680,-125,canvas)
p2 = createTurtlePlayer('blue',-680,-50,canvas)
p3 = createTurtlePlayer('green',-680,25,canvas)
p4 = createTurtlePlayer('yellow',-680,100,canvas)

forwardp1 = 0
forwardp2 = 0 
forwardp3 = 0
forwardp4 = 0 
matchno = 1

def newgame():
    global forwardp1
    global forwardp2 
    global forwardp3
    global forwardp4 
    global matchno
    p1.backward(forwardp1)
    p2.backward(forwardp2)
    p3.backward(forwardp3)
    p4.backward(forwardp4)
    forwardp1 = 0
    forwardp2 = 0
    forwardp3 = 0
    forwardp4 = 0
    text1.delete("1.0","end")
    matchno = matchno + 1


def move():
    global forwardp1
    global forwardp2 
    global forwardp3
    global forwardp4 
    
    a = (random.randint(1,3))*50
    b = (random.randint(1,3))*50
    c = (random.randint(1,3))*50
    d = (random.randint(1,3))*50
    
    global matchno
    if(p1.xcor()>500 or p2.xcor()> 500 or p3.xcor()> 500 or p3.xcor()> 500 or p4.xcor()> 500):
        if(p1.xcor()> 500):
            p1.forward(a)
            forwardp1 = forwardp1 + a
            printfin(text1,'Red ')
            updatescore(matchno,1,0,0,0)
            printscore(text2,matchno)
            newgame()
            return
        if(p2.xcor()> 500):
            p2.forward(b)
            forwardp2 = forwardp2 + b
            printfin(text1,'Blue ')
            updatescore(matchno,0,1,0,0)
            printscore(text2,matchno)
            newgame()
            return
        if(p3.xcor()> 500):
            p3.forward(c)
            forwardp3 = forwardp3 + c
            printfin(text1,'Green ')
            updatescore(matchno,0,0,1,0)
            printscore(text2,matchno)
            newgame()
            return
        if(p4.xcor()> 500):
            p4.forward(d)
            forwardp4 = forwardp4 + d
            printfin(text1,'Yellow ')
            updatescore(matchno,0,0,0,1)
            printscore(text2,matchno)
            newgame()
            return
    
    p1.forward(a)
    p2.forward(b)
    p3.forward(c)
    p4.forward(d)

    forwardp1 = forwardp1 + a
    forwardp2 = forwardp2 + b
    forwardp3 = forwardp3 + c
    forwardp4 = forwardp4 + d


def quit():
    window.destroy()
    global forwardp1
    global forwardp2 
    global forwardp3
    global forwardp4
    global matchno 
    forwardp1 = 0
    forwardp2 = 0
    forwardp3 = 0
    forwardp4 = 0
    matchno = 1
    con= sqlite3.connect('scorekeep.db')
    cur = con.cursor()
    cur.execute('DROP TABLE Score')


text1 = tk.Text(window, width=30,height=1,font="Arial 15")
text1.pack(pady=10,side="top")
text2 = tk.Text(window, width=45,height=5,font="Arial 15")
text2.pack(pady=20,side="bottom")
text2.insert(tk.INSERT,"Number of games played : 0")
button3 = tk.Button(window, text="NEW GAME",bg="#9BE3DE",relief="raised",borderwidth=4, width=15,height=4,command=newgame)
button3.pack(padx=65,side="left")
button5 = tk.Button(window, text="MOVE",bg="#9BE3DE",relief="raised",borderwidth=4, width=15,height=4,command=move)
button5.pack(padx=65,side="right")
button4 = tk.Button(window, text="CLOSE",bg="#9BE3DE",relief="raised",borderwidth=4 ,width=15,height=4,command=quit)
button4.pack(padx=43,side="right")

window.mainloop()