import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="Witj świecie")
        self.values = tkinter.StringVar()
        self.label2 = tkinter.Label(self.top_frame, textvariable=self.values)
        self.label3 = tkinter.Label(self.bottom_frame, text="Python")
        self.label4 = tkinter.Label(self.bottom_frame, text="Python2")

        self.button = tkinter.Button(self.bottom_frame, text="Ok", command=self.do_it)

        self.label1.pack(side='left', pady=10)
        self.label2.pack(side='top')
        self.label3.pack(side='left')
        self.label4.pack(side='right', ipadx=10)

        self.button.pack(side="bottom")
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_it(self):
        print("Wcisnąłeś ok")
        self.values.set("STOP")


my_gui = MyGui()
