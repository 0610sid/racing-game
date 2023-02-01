import sqlite3
import tkinter as tk

def createtable():
    con= sqlite3.connect('scorekeep.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE Score(M INTEGER, P1 INTEGER , P2 INTEGER , P3 INTEGER, P4 INTEGER)')
    con.commit()

def updatescore(a,b,c,d,e):
    con= sqlite3.connect('scorekeep.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Score VALUES(?,?,?,?,?)',(a,b,c,d,e))
    con.commit()

def printscore(t,b):
    con= sqlite3.connect('scorekeep.db')
    cur = con.cursor()
    cur.execute('SELECT SUM(P1) FROM Score')
    sp1 = cur.fetchall()
    cur.execute('SELECT SUM(P2) FROM Score')
    sp2 = cur.fetchall()
    cur.execute('SELECT SUM(P3) FROM Score')
    sp3 = cur.fetchall()
    cur.execute('SELECT SUM(P4) FROM Score')
    sp4 = cur.fetchall()

    t.delete("1.0","end")

    t.insert(tk.INSERT,"Total numbers of matches played : "+str(b)+"\n")
    t.insert(tk.INSERT,"Number of matches won by Red   :   "+str(sp1)[2:4]+"\n")
    t.insert(tk.INSERT,"Number of matches won by Blue   :   "+str(sp2)[2:4]+"\n")
    t.insert(tk.INSERT,"Number of matches won by Green  : "+str(sp3)[2:4]+"\n")
    t.insert(tk.INSERT,"Number of matches won by Yellow : "+str(sp4)[2:4]+"\n")