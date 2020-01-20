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
        self.controller = controller

        topFrame = tk.Frame(self, height=0 + 15)
        topFrame.grid(column=0, row=0)

        leftFrame = tk.Frame(self, width=0 + 200)
        leftFrame.grid(column=0, row=0)

        centerFrame = tk.Frame(self, height=45)
        centerFrame.grid(column=0, row=4)

        label = tk.Label(self, text="Administrator", font=LARGE_FONT)
        label.grid(column=1, row=1)

        button2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame(Gui.PageOne))
        button2.grid(column=1, row=3)
        ######################### Browse a file ########################
        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.grid()

        self.browseButton = ttk.Button(self.labelFrame, text="Browse A Song Parameters File", command=self.fileDialog)
        self.browseButton.grid(column=1, row=1, pady=4)

        self.trainButton = ttk.Button(self.labelFrame, text="Browse A Song Parameters File", command=self.trainDB)
        self.trainButton.grid(column=1, row=2, pady=4)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.csv"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=2, row=1)
        self.label.configure(text=self.filename)

        ######################### Browse a file ########################

    def trainDB(self):
        dbName = self.filename