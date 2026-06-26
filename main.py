from tkinter import *

result = ''


def show_result(value):
    global result
    result += value
    result_label.config(text=result)


def clear():
    global result
    result = ''
    result_label.config(text=result)


def caculate():
    global result
    mainresultresult = ''
    if result != '':
        try:
            mainresult = eval(result)
        except (SyntaxError, TypeError):
            mainresult = 'فرمت وارد شده صحیح نمی باشد'
            result = ''
    result_label.config(text=mainresult)


def backspace():
    global result
    result = result[:-1]
    result_label.config(text=result)


window = Tk()
window.title('Calculator')
window.geometry('600x600+500+200')
window.resizable(False, False)
window.configure(bg="#070B1D")

result_label = Label(window, text='', font=('', 33, 'bold'))
result_label.place(width=590, height=100, x=4, y=10)


# Buttons of row 1
button1 = Button(window, text='C', font=('', 41, 'bold'),
                 bg="#0059ff", fg='white', bd=6, command=clear)
button1.place(width=135, height=75, x=18, y=150)

button2 = Button(window, text='/', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('/'))
button2.place(width=75, height=75, x=163, y=150)

button3 = Button(window, text='(', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('('))
button3.place(width=50, height=75, x=249, y=150)

button4 = Button(window, text=')', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result(')'))
button4.place(width=50, height=75, x=308, y=150)

button4 = Button(window, text='%', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('%'))
button4.place(width=75, height=75, x=368, y=150)

button6 = Button(window, text='X', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('*'))
button6.place(width=135, height=75, x=453, y=150)


# Buttons of row 2
button7 = Button(window, text='7', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('7'))
button7.place(width=135, height=75, x=18, y=240)

button8 = Button(window, text='8', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('8'))
button8.place(width=135, height=75, x=163, y=240)

button9 = Button(window, text='9', font=('', 30, 'bold'),
                 bg="#1a2634", fg='white', bd=4, command=lambda: show_result('9'))
button9.place(width=135, height=75, x=308, y=240)

button10 = Button(window, text='-', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('-'))
button10.place(width=135, height=75, x=453, y=240)


# Buttons of row 3
button11 = Button(window, text='4', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('4'))
button11.place(width=135, height=75, x=18, y=330)

button12 = Button(window, text='5', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('5'))
button12.place(width=135, height=75, x=163, y=330)

button13 = Button(window, text='6', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('6'))
button13.place(width=135, height=75, x=308, y=330)

button14 = Button(window, text='+', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('+'))
button14.place(width=135, height=75, x=453, y=330)


# Buttons of row 4
button15 = Button(window, text='1', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('1'))
button15.place(width=135, height=75, x=18, y=420)

button16 = Button(window, text='2', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('2'))
button16.place(width=135, height=75, x=163, y=420)

button17 = Button(window, text='3', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('3'))
button17.place(width=135, height=75, x=308, y=420)

button18 = Button(window, text='=', font=('', 30, 'bold'),
                  bg="#0059ff", fg='white', bd=4, command=caculate)
button18.place(width=135, height=165, x=453, y=420)


# Buttons of last row
button19 = Button(window, text='0', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('0'))
button19.place(width=135, height=75, x=18, y=510)

button20 = Button(window, text='.', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('.'))
button20.place(width=135, height=75, x=163, y=510)

button21 = Button(window, text='^', font=('', 30, 'bold'),
                  bg="#1a2634", fg='white', bd=4, command=lambda: show_result('**'))
button21.place(width=135, height=75, x=308, y=510)


# Backspace button
button22 = Button(window, text='Back', font=('', 15, 'bold'),
                  bg="#b60000", fg='white', bd=4, command=backspace)
button22.place(width=70, height=28, x=518, y=117)

mainloop()
