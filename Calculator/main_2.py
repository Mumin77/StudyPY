from tkinter import *
from tkinter import ttk

operation = ''
temp_number = 0
#결과 출력 상태인지 상태 저장
answer_trigger = False

# 함수 추가 공간
def btn_press(value):
    global operation
    global answer_trigger

    if value =='AC': # AC버튼 눌렀을때 실행되는 것
        num_ety.delete(0,'end')
        operation = ''
        answer_trigger = False
        print("AC가 눌렸버렸다...")
    else: # 그 외 숫자일 때 실행되는 것
        if answer_trigger:
            num_ety.delete(0,'end')
            answer_trigger = False
        num_ety.insert("end",value) # 텍스트 창으로 숫자를 전송한다. 'end'는 오른쪽 끝에 추가하라는 뜻
        print(value,'눌려버렸다...')

#소수점으로 int형 변환 시 에러가 날 경우, float형으로 반환시켜 계산하도록 만듬
def float_filter(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return float(value)

def math_btn_press(value):
    global operation #함수 바깥의 글로벌 변수 사용
    global temp_number
    global answer_trigger
    if not num_ety.get() == '': # 기존에 입력한 숫자가 있을 때만 연산 버튼 인식
        operation = value
        temp_number = float_filter(num_ety.get()) # 입력된 숫자를 임시 변수로 옮긴다. float_filter함수 호출
        num_ety.delete(0,'end') # 입력칸을 비우고 다음 숫자를 입력 받을 준비
        print(temp_number, operation) #

def equal_btn_press(): # =버튼 계산
    global operation
    global temp_number
    global answer_trigger
    #연산자나 숫자가 입력되지 않으면 실행이 앙대요!
    if not (operation == '' and num_ety.get()==''):
        num = int(num_ety.get())
        if operation == '/':
            solution = temp_number/num
        elif operation == '*':
            solution = temp_number*num
        elif operation == '+':
            solution = temp_number+num
        else :
            solution = temp_number-num
            # 계산 후 숫자 표시 칸을 비우고, 계산 결과를 표시
            num_ety.delete(0,'end')
            num_ety.insert(0,solution)
            print(temp_number,operation,num,"=",solution)
            operation = ''
            temp_number = 0
            # 계산 완료 후 Trigger 변수 True로 변경
            answer_trigger =True

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
