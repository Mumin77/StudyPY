from tkinter import *
from tkinter import ttk

# 함수 추가 공간
def btn_press(value):
    num_ety.insert("end",value) # 텍스트 창으로 숫자를 전송한다. 'end'는 오른쪽 끝에 추가하라는 뜻
    print(value,'눌려버렸다...')

def math_btn_press(value):
    print(value, '사칙연산눌려버렸다...') #사칙연산 버튼 계산

def equal_btn_press(): # =버튼 계산
    print("이꼴 눌려버렸다...")

root = Tk()
root.title("진짜 계산기")
root.geometry("350x200")

#텍스트 창의 값을 저장한 변수
ety_value = StringVar(root, value='')

#숫자 및 결과 표시창
num_ety = ttk.Entry(root, textvariable = ety_value,width=35)
num_ety.grid(row=0, columnspan=4)

#인터페이스 (버튼,창) 추가 부분

#숫자 버튼

btn1 = ttk.Button(root, text = "1", command=lambda :btn_press("1"))
btn1.grid(row=1, column=0)

btn2 = ttk.Button(root, text = "2", command=lambda :btn_press("2"))
btn2.grid(row=1, column=1)

btn3 = ttk.Button(root, text = "3", command=lambda :btn_press("3"))
btn3.grid(row=1, column=2)

btn_div = ttk.Button(root, text='/', command = lambda : math_btn_press("/")) #나누기 버튼
btn_div.grid(row =1 , column = 3)


btn4 = ttk.Button(root, text = "4", command=lambda :btn_press("4"))
btn4.grid(row=2, column=0)

btn5 = ttk.Button(root, text = "5", command=lambda :btn_press("5"))
btn5.grid(row=2, column=1)

btn6 = ttk.Button(root, text = "6", command=lambda :btn_press("6"))
btn6.grid(row=2, column=2)

btn_mult = ttk.Button(root, text="*", command = lambda :math_btn_press("*")) #곱하기 버튼
btn_mult.grid(row=2, column=3)


btn7= ttk.Button(root, text = "7", command=lambda :btn_press("7"))
btn7.grid(row=3, column=0)

btn8 = ttk.Button(root, text = "8", command=lambda :btn_press("8"))
btn8.grid(row=3, column=1)

btn9 = ttk.Button(root, text = "9", command=lambda :btn_press("9"))
btn9.grid(row=3, column=2)

btn_add = ttk.Button(root, text = "+", command = lambda : math_btn_press("+"))
btn_add.grid(row=3, column=3)


#마지막줄 AC,0,=,- 버튼추가
# -버튼 -> math_button_pressed() 로 연결.
# AC,0 버튼 -> button_pressed() 로 연결
# = 버튼 -> equal_button_pressed() 로 연결
button_ac = ttk.Button(root, text="AC", command = lambda:btn_press('AC'))
button_ac.grid(row=4, column=0)

button0 = ttk.Button(root, text="0", command = lambda:btn_press('0'))
button0.grid(row=4, column=1)

button_equal = ttk.Button(root, text="=", command = lambda:equal_btn_press())
button_equal.grid(row=4, column=2)

button_sub = ttk.Button(root, text="-", command = lambda:math_btn_press('-'))
button_sub.grid(row=4, column=3)


root.mainloop()
