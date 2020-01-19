import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

# def printFeelings():
#     print("I love Tomer Shmilovitz!!")

# root = Tk("Galits Window") #create instance of a blanck window

# label1 = Label(root, text="Name")  #create instance of a blanck label
# label2 = Label(root, text="ID")
#
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# label1.grid(row=0, sticky=E)
# entry1.grid(row=0, column=1)
# label2.grid(row=1, sticky=E)
# entry2.grid(row=1, column=1)
#
# checkBox1 = Checkbutton(root, text="keep me logged in")
# checkBox1.grid(columnspan=2)

# def printFeelings(event):
#     print("I love Tomer Shmilovitz!!")

## ****** Menu ********
# menu1 = Menu(root)
# root.config(menu=menu1)
#
# subMenu1 = Menu(menu1)
# menu1.add_cascade(label="File", menu=subMenu1)
# subMenu1.add_command(label="print my feelings", command=printFeelings)
#
# # ****** Toolbar ********
#
# toolBar = Frame(root, bg="blue")
# insertBTN1 = Button(toolBar, text="print my feelings", command=printFeelings)
# insertBTN1.grid(sticky=W+E+N+S)
# insertBTN2 = Button(toolBar, text="print my feelings", command=printFeelings)
# insertBTN2.grid(row=0, column=1, padx=1, sticky=W+E+N+S)
#
# toolBar.pack(fill=X)
#
# # ****** Status Bar ********
# status = Label(root, text="I will love my Tomer...", bd=1, relief=SUNKEN, anchor=W) #bd id board deep
# status.pack(side=BOTTOM, fill=X)
#
# ****** Message Window ********
# tkinter.messagebox.showinfo("what should i write here? ho right, I love Tomer!")

# answer = tkinter.messagebox.askquestion("Question1:", "Do you like dogs?")
# if answer == 'yes':
#     print("<3")
#
##********** photo image **********
# photo = PhotoImage(file="microphoneBackground.png")
# laberForPhoto = Label(root, image=photo)
# laberForPhoto.pack(fill=BOTH)





# label1.pack() #puts label in first place it can
#
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(text="Print my feelings", fg='blue', command=printFeelings)    #fg is the color of the font of the button, bg is the backround
# button1 = Button(text="Print my feelings", fg='blue')
# button1.bind("<Button-3>", printFeelings)
# button1.pack()
# # button2 = Button(topFrame, text="button2", fg='blue')
# button3 = Button(topFrame, text="button3", fg='green')
# button4 = Button(bottomFrame, text="button4", fg='purple')
#

# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)



# root.mainloop() #an infinit loop to run this window

LARGE_FONT= ("Verdana", 12)

# class LoginGUI(Frame):
#     def __init__(self, master): #master is root
#         frameBg = Frame(master)
#         frameBg.pack(fill=BOTH, expand=True)
#
#         self.image = Image.open("microphoneBackground.png")
#         self.img_copy = self.image.copy()
#
#         self.background_image = ImageTk.PhotoImage(self.image)
#
#         self.background_label = Label(frameBg, image=self.background_image)
#         self.background_label.pack(fill=BOTH, expand=YES)
#         self.background_label.bind('<Configure>', self._resize_image)
#
#         self.labelTextID = StringVar()
#         self.labelTextID.set("ID")
#         self.labelDirID = Label(self.background_label, textvariable=self.labelTextID)
#         self.labelDirID.grid(column=0, row=0, padx=5, sticky=E)
#
#         self.entryTextID = StringVar()
#         self.entryTextID.set("Insert your ID")
#         self.entryID = Entry(self.background_label, textvariable=self.entryTextID, width=20)
#         self.entryID.grid(column=1, row=0)
#
#         self.labelTextPassword = StringVar()
#         self.labelTextPassword.set("Password")
#         self.labelPassword = Label(self.background_label, textvariable=self.labelTextPassword)
#         self.labelPassword.grid(column=0, row=1, padx=5)
#
#         self.entryTextPassword = StringVar()
#         self.entryTextPassword.set("Insert your Password")
#         self.entryPassword = Entry(self.background_label, textvariable=self.entryTextPassword, width=20)
#         # self.entryName.pack(side=LEFT,anchor=W, expand=YES)
#         self.entryPassword.grid(column=1, row=1, sticky=E)
#
#         self.loginButton = Button(self.background_label, text="Login", command=self.loginFunc)
#         self.loginButton.grid(column=1, row=2)
#         #
#         # self.quitButton = Button(background_label, text="Quit", command=frame.quit)
#         # self.quitButton.grid(row=2, column=1)
#         # answer = tk.messagebox.askquestion("Question1:", "Do you like dogs?")
#         # if answer == 'yes':
#         #     print("<3")
#         # else:
#         #     pass
#
#     def loginFunc(self):
#         print("loging funck")
#         IDAns = self.entryID.get()
#         print(IDAns)
#         PasswordAns = self.entryPassword.get()
#         print(PasswordAns)

# class MainGUI(Frame):
#     def __init__(self, master):  # master is root
#         frameBg = Frame(master)
#         frameBg.pack(fill=BOTH, expand=True)
#
#         self.image = Image.open("microphoneBackground.png")
#         self.img_copy = self.image.copy()
#
#         self.background_image = ImageTk.PhotoImage(self.image)
#
#         self.background_label = Label(frameBg, image=self.background_image)
#         self.background_label.pack(fill=BOTH, expand=YES)
#         self.background_label.bind('<Configure>', self._resize_image)
#
#         self.UserButton = Button(self.background_label, text="User", command=self.UserFunc)
#         self.UserButton.grid(column=1, row=2)
#         #
#         # self.quitButton = Button(background_label, text="Quit", command=frame.quit)
#         # self.quitButton.grid(row=2, column=1)
#         # answer = tk.messagebox.askquestion("Question1:", "Do you like dogs?")
#         # if answer == 'yes':
#         #     print("<3")
#         # else:
#         #     pass
#
#     def _resize_image(self, event):
#         new_width = event.width
#         new_height = event.height
#
#         self.image = self.img_copy.resize((new_width, new_height))
#         self.background_image = self.img_copy.resize((new_width, new_height), Image.ANTIALIAS)
#
#         self.background_image = ImageTk.PhotoImage(self.image)
#         self.background_label.configure(image=self.background_image)
#
#     def UserFunc(self):
#         print("UserFunc")


import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainGUI, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainGUI)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MainGUI", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainGUI))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainGUI))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

def main():
    app = SeaofBTCapp()
    app.mainloop()


if __name__ == '__main__':
    main()
