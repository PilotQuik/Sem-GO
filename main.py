import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Label
from events import Event
from const import *
from menu import Menu
from game import Game


class Root(tk.Tk): # defines Main class inheriting from tk.TK
    def __init__(self):
        super().__init__() # initializing tkinter

        self.iconbitmap("assets/icon.ico")

        self.frame = Menu(self)
        self.event = Event(self)

    def findCenter(self, winHeight, winWidth):
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        centerX = int(screenWidth / 2 - winWidth / 2)
        centerY = int(screenHeight / 2 - winHeight / 2)
        return (centerX, centerY)

    def switchFrame(self, newFrame):
        self.frame.pack_forget()
        self.frame = newFrame(self)

if __name__ == "__main__":
    root = Root() # creating instance of Main class
    root.bind("<Button-1>", root.event.mouse1) # leftclick-event
    root.mainloop()