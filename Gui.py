import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import GraphsGui

LARGE_FONT = ("Verdana", 18)


class GuiController(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x400-300+100")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.pack(side=TOP, fill=BOTH, expand=True)

        frameBg = Frame(self)
        frameBg.pack(fill=BOTH, expand=True)

        self.image = Image.open("microphoneBackground.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background_label = Label(frameBg, image=self.background_image)
        self.background_label.pack(fill=BOTH, expand=YES)
        self.background_label.bind('<Configure>', self._resize_image)

        self.frames = {}

        for F in (MainGUI,
                  PageOne,
                  PageTwo,
                  GraphsGui.GraphsPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainGUI)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def _resize_image(self, event):
        self.new_width = event.width
        self.new_height = event.height

        self.image = self.img_copy.resize((self.new_width, self.new_height))
        self.background_image = self.img_copy.resize((self.new_width, self.new_height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background_label.configure(image=self.background_image)

class MainGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self, height=0+15)
        topFrame.grid(column=0, row=0)

        leftFrame = tk.Frame(self, width=0+250)
        leftFrame.grid(column=0, row=0)

        centerFrame = tk.Frame(self, height=45)
        centerFrame.grid(column=0, row=4)

        label = tk.Label(self, text="Main", font=LARGE_FONT)
        label.grid(column=1, row=1, pady=3)

        button = tk.Button(self, text="User",
                           command=lambda: controller.show_frame(PageOne))
        button.grid(column=1, row=2, pady=3)

        button2 = tk.Button(self, text="Administrator",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(column=1, row=3, pady=3)

        button3 = tk.Button(self, text="Visit Administrator Page",
                            command=lambda: controller.show_frame(GraphsGui.GraphsPage))
        button3.grid(column=1, row=4, pady=3)




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        topFrame = tk.Frame(self, height=0 + 15)
        topFrame.grid(column=0, row=0)

        leftFrame = tk.Frame(self, width=0 + 225)
        leftFrame.grid(column=0, row=0)

        centerFrame = tk.Frame(self, height=45)
        centerFrame.grid(column=0, row=4)

        label = tk.Label(self, text="User", font=LARGE_FONT)
        label.grid(column=1, row=1)

        button = tk.Button(self, text="Main", command=lambda: controller.show_frame(MainGUI))
        button.grid(column=1, row=2)

        button2 = tk.Button(self, text="Administrator", command=self.loginFunc)
        button2.grid(column=1, row=3)

    def loginFunc(self):
        print("user loging funck")
        # IDAns = self.entryID.get()
        # print(IDAns)
        # self.entryTextID.set("gggg")
        # PasswordAns = self.entryPassword.get()
        # print(PasswordAns)
        # self.controller.show_frame(PageTwo)
        answer = tk.messagebox.askquestion("Question1:", "Are you sure you want to go to admin?")
        if answer == 'yes':
            self.controller.show_frame(PageTwo)
        else:
            pass



class PageTwo(tk.Frame):

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

        button = tk.Button(self, text="Main", command=lambda: controller.show_frame(MainGUI))
        button.grid(column=1, row=2)

        button2 = tk.Button(self, text="User", command=lambda: controller.show_frame(PageOne))
        button2.grid(column=1, row=3)

def main():
    app = GuiController()
    app.mainloop()


if __name__ == '__main__':
    main()
