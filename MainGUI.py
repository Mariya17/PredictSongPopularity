import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
# from PageThree import PageThree as PageThree
# import Gui.PageOne as PageOne

LARGE_FONT = ("Verdana", 18)

class MainGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self, height=0+15)
        topFrame.grid(column=0, row=0)

        leftFrame = tk.Frame(self, width=0+250)
        leftFrame.grid(column=0, row=0)

        centerFrame = tk.Frame(self, height=45)
        centerFrame.grid(column=0, row=40)

        label = tk.Label(self, text="Main", font=LARGE_FONT)
        label.grid(column=1, row=1)

        button = tk.Button(self, text="User",
                           command=lambda: controller.show_frame(PageOne))
        button.grid(column=1, row=2, pady=3)

        button2 = tk.Button(self, text="Administrator",
                            command=lambda: controller.show_frame(PageThree))
        button2.grid(column=1, row=3)

        button2 = tk.Button(self, text="Three",
                            command=lambda: controller.show_frame(PageThree))
        button2.grid(column=1, row=4)
