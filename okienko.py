import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text="Witj świecie")
        self.label2 = tkinter.Label(self.main_window, text="Python")

        self.label1.pack(side='left', pady=10)
        self.label2.pack(side='top')

        tkinter.mainloop()


my_gui = MyGui()
