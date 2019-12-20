
import tkinter as tk

calc = tk.Tk()

#창 세부설정

calc.title("계산기")
calc.geometry("300x300")

def calculate(event):  #func 이라는 함수를 설정
    value = tk.Entry.get(display)
    if value != '':
       result = eval(value)
       print(result)    # eval 이라는 함수를 이용해 display안에 있는 값을 계산함
       display.delete(0,tk.END) #(내용 삭제) 0번째 자리부터 끝까지 삭제하는 명령어
       display.insert(0,result) # (새 값을 입력) 0번째 자리에 result 변수 값을 입력하는 명령어

def clear(event) :
    display.delete(0,tk.END)


display = tk.Entry(calc , width  = 20)  # display라는 이름의 Entry창, 폭은 20이다.
display.pack()  #위치를 정해주는 명령어

button_e = tk.Button(calc, text='=', width=5)  # = 버튼 추가
button_e.bind('<Button-1>', calculate)  # 버튼에 클릭 이벤트 추가
button_e.pack()

button_c = tk.Button(calc, text='c', width=5)  # C버튼추가. text속성은 버튼에 표시할 문자입니다.
button_c.bind('<Button-1>', clear)  # <Button-1> 이벤트는 마우스 왼쪽클릭 이벤트입니다.
button_c.pack()

calc.bind('<Return>', calculate) #엔터키(이벤트)를 func 함수에서 불러온다
calc.bind('Escape', clear)

calc.mainloop()

