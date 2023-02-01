import turtle
import tkinter as tk

def createTurtlePlayer(abc, startx, starty, xyz):

    player=turtle.RawTurtle(xyz)
    player.shape('turtle')
    player.color(abc)
    player.penup() 
    player.goto(startx, starty)
    return player

def printfin(a,b):
    a.insert(tk.INSERT,b+"is the winner")