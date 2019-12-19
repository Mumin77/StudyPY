
import tkinter as tk

calc = tk.Tk()

#창 세부설정

calc.title("계산기")
calc.geometry("300x300")

def func(event):  #func 이라는 함수를 설정
    print(tk.Entry.get(display)) # display라는 변수 안에 있는 Entry값을 가져오는 것

display = tk.Entry(calc , width  = 20)  # display라는 이름의 Entry창, 폭은 20이다.
display.pack()  #위치를 정해주는 명령어

calc.bind('<Return>', func) #엔터키(이벤트)를 func 함수에서 불러온다

calc.mainloop()

