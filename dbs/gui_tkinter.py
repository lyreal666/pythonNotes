#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

from tkinter import *
import tkinter.messagebox as messagebox

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_name = Entry(self)
        self.input_name.pack()
        self.hello_label = Label(self, text='hello tk')
        self.hello_label.pack()
        self.alert_button = Button(self, text='hello', command=self.hello)
        self.alert_button.pack()
        self.exit_button = Button(self, text='exit', command=self.quit)
        self.exit_button.pack()

    def hello(self):
        name = self.input_name.get() or 'world'
        messagebox.showinfo('message', 'hello %s!' % name)


app1 = App()
app1.master.title('hello tk')
app1.mainloop()