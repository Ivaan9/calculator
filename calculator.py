
from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.frame2 = CTkFrame(self, width=300, height=450, fg_color='#77fce2', corner_radius=30)
        self.btn = CTkButton(self, text='7', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.seven)
        self.btn2 = CTkButton(self, text='8', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.eight)
        self.btn3 = CTkButton(self, text='9', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.nine)
        self.btn4 = CTkButton(self, text='4', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.four)
        self.btn5 = CTkButton(self, text='5', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.five)
        self.btn6 = CTkButton(self, text='6', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.six)
        self.btn7 = CTkButton(self, text='1', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.one)
        self.btn8 = CTkButton(self, text='2', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.two)
        self.btn9 = CTkButton(self, text='3', font=("LCD Mono", 25), text_color='black', fg_color='white', width=50, height=50, command=self.three)
        self.btn10 = CTkButton(self, text='0', font=("LCD Mono", 25), text_color='black', fg_color='white', width=170, height=50, command=self.zero)
        self.btn11 = CTkButton(self, text='×', font=("LCD Mono", 25), text_color='white', fg_color='#fc03a9', width=50, height=50)
        self.btn12 = CTkButton(self, text='÷', font=("LCD Mono", 25), text_color='white', fg_color='#fc03a9', width=50, height=50)
        self.btn13 = CTkButton(self, text='-', font=("LCD Mono", 25), text_color='white', fg_color='#fc03a9', width=50, height=50)
        self.btn14 = CTkButton(self, text='=', font=("LCD Mono", 25), text_color='white', fg_color='#fc03a9', width=50, height=50, command=self.dorin)
        self.btn15 = CTkButton(self, text='C', font=("LCD Mono", 25), text_color='black', fg_color='white', width=110, height=50, command=self.c)
        self.btn16 = CTkButton(self, text='+', font=("LCD Mono", 25), text_color='white', fg_color='#fc03a9', width=50, height=50, command=self.plus)
        self.entry = CTkEntry(self, font=("LCD Mono", 40), width=247, placeholder_text='' , height=70, corner_radius=12, border_color='#1a001f')
        self.lable = CTkLabel(self, text='', font=("LCD Mono", 40))

        self.btn.place(x=200, y=180)
        self.btn2.place(x=260, y=180)
        self.btn3.place(x=320, y=180)
        self.btn4.place(x=200, y=245)
        self.btn5.place(x=260, y=245)
        self.btn6.place(x=320, y=245)
        self.btn7.place(x=200, y=310)
        self.btn8.place(x=260, y=310)
        self.btn9.place(x=320, y=310)
        self.btn10.place(x=200, y=370)
        self.btn11.place(x=400, y=180)
        self.btn12.place(x=400, y=245)
        self.btn13.place(x=400, y=310)
        self.btn14.place(x=400, y=370)
        self.btn15.place(x=200, y=120)
        self.btn16.place(x=400, y=120)
        self.entry.place(x=200, y=40)
        self.frame2.place(x=175, y=10)
    def one(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text+'1')
    def two(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '2')
    def three(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '3')
    def four(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '4')
    def five(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '5')
    def six(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '6')
    def seven(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '7')
    def eight(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '8')
    def nine(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '9')
    def zero(self):
        self.entry.configure(placeholder_text=self.entry._placeholder_text + '0')
    def c(self):
        self.entry.configure(placeholder_text="")
    def plus(self):
        global a
        global c
        c = "+"
        a=self.entry._placeholder_text
        self.entry.configure(placeholder_text="")
    def dorin(self):
        global b
        b = self.entry._placeholder_text
        if c == "+":
            self.entry.configure(placeholder_text=int(a)+int(b))
window = MainWindow()
window.mainloop()
#test