from tkinter import *
root = Tk()
root.title("키보드 계산기")
root.geometry('300x200')


def key_input(val):
    print(val)
    print(val.char)
    print(repr(val.char))


root.bind('<key>',key_input)


