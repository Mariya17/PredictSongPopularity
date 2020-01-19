import Gui
from Gui import MainGUI
import GuiWorks
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog

LARGE_FONT = ("Verdana", 12)

class GraphsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Admin Page!!!", font=LARGE_FONT)
        self.label.pack(pady=30, padx=30)
        self.controller = controller

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(MainGUI))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", command=self.loginFunc)
        button2.pack()
        ######################### Browse a file ########################
        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.pack()

        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse A File", command=self.fileDialog)
        self.button.grid(column=1, row=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.csv"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)

        ######################### Browse a file ########################
    def loginFunc(self):
        print("loging funck")
        # IDAns = self.entryID.get()
        # print(IDAns)
        # self.entryTextID.set("gggg")
        # PasswordAns = self.entryPassword.get()
        # print(PasswordAns)
        lambda: self.controller.show_frame(GraphsPage)