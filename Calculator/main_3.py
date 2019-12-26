from tkinter import *
root = Tk()
root.title("키보드 계산기")
root.geometry('300x200')


def key_input(value):
    # 쉬프트키 입력 무시.(덧셈할때)
    if not repr(value.char) == "''":
        numbers = '1234567890'
        operators = '/*+-'
        # 숫자키 입력시, button_pressed()함수 호출.
        if value.char in numbers :
            button_pressed(value.char)
            print(value.char)
        # 연산자 입력시, math_button_pressed() 함수 호출.
        elif value.char in operators :
            math_button_pressed(value.char)
            print(value.char)
        # 엔터키 입력 -> =버튼
        elif value.keysym == "Return":
            equal_button_pressed()
            print("equal button pressed")
        # ESC 키 입력. -> AC 버튼 입력.
        elif value.keysym == "Escape":
            button_pressed('AC')
            print('AC button pressed')
        # BackSpace 입력시, 마지막 한글자 삭제.
        elif value.keysym == "BackSpace":
            number_entry.delete(len(number_entry.get())-1,'end')
            print(number_entry)


root.bind('<key>',key_input)


