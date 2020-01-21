import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
# from MainGUI import MainGUI as MainGUI


LARGE_FONT = ("Verdana", 12)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self, height=0 + 15)
        topFrame.grid(column=0, row=0)

        leftFrame = tk.Frame(self, width=0 + 225)
        leftFrame.grid(column=0, row=0)

        centerFrame = tk.Frame(self, height=45)
        centerFrame.grid(column=0, row=4)

        label = tk.Label(self, text="Test", font=LARGE_FONT)
        label.grid(column=1, row=1)

        button = tk.Button(self, text="Main", command=lambda: controller.show_frame(MainGUI))
        button.grid(column=1, row=2)

        button2 = tk.Button(self, text="Administrator", command=lambda: controller.show_frame(PageThree))
        button2.grid(column=1, row=3)