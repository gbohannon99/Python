#Calculator Program 

from tkinter import * 

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    
    try:
        total = str(eval(equation_text))

        equation_label.set(total)
        
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
    
    except SyntaxError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
        
def clear():
    global equation_text

    equation_label.set("")
    equation_text=""



#Initializing the Window
window = Tk()

window.title("Calculator Program")
window.geometry("500x500")

#Creating a string that will store the numbers
equation_text = ""

#Creating an empty variable for storing the label of the calculator
equation_label = StringVar()

#Creating a Label that will display the numbers, etc. 
label = Label(window, textvariable=equation_label,
              font=('consolas',20),
              bg = "White",
              width=24,
              height=2)
label.pack()

#This Frame is to help organize the Calculator Buttons into a grid 
frame = Frame(window)
frame.pack()

#Number Buttons 1 - 3 
button1 = Button(frame, text = 1, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(1))
button1.grid(row = 0, column = 0 )

button2 = Button(frame, text = 2, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(2))
button2.grid(row = 0, column = 1 )

button3 = Button(frame, text = 3, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(3))
button3.grid(row = 0, column = 2 )

#Number Buttons 4 - 6
button4 = Button(frame, text = 4, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(4))
button4.grid(row = 1, column = 0 )

button5 = Button(frame, text = 5, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(5))
button5.grid(row = 1, column = 1 )

button6 = Button(frame, text = 6, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(6))
button6.grid(row = 1, column = 2 )

#Number Buttons 7 - 9
button7 = Button(frame, text = 7, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(7))
button7.grid(row = 2, column = 0 )

button8 = Button(frame, text = 8, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(8))
button8.grid(row = 2, column = 1 )

button9 = Button(frame, text = 9, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(9))
button9.grid(row = 2, column = 2 )

button0 = Button(frame, text = 0, height = 4, width = 9, font = 35, 
                 command = lambda: button_press(0))
button0.grid(row = 3, column = 0 )

#Arithmetic symbols (+, -, /, *)
Plus = Button(frame, text = '+', height = 4, width = 9, font = 35, 
                 command = lambda: button_press('+'))
Plus.grid(row = 0, column = 3 )

Minus = Button(frame, text = '-', height = 4, width = 9, font = 35, 
                 command = lambda: button_press('-'))
Minus.grid(row = 1, column = 3 )

Multiply = Button(frame, text = '*', height = 4, width = 9, font = 35, 
                 command = lambda: button_press('*'))
Multiply.grid(row = 2, column = 3 )

Divide = Button(frame, text = '/', height = 4, width = 9, font = 35, 
                 command = lambda: button_press('/'))
Divide.grid(row = 3, column = 3 )


#Other Symbols (., =, clear)
Equal = Button(frame, text = '=', height = 4, width = 9, font = 35, 
                 command = equals)
Equal.grid(row = 3, column = 2 )

Decimal = Button(frame, text = '.', height = 4, width = 9, font = 35, 
                 command = lambda: button_press('.'))
Decimal.grid(row = 3, column = 1 )

Clear = Button(frame, text = 'clear', height = 4, width = 9, font = 35, 
                 command = clear)
Clear.grid(row = 4, column = 0 )


#Deploying the window
window.mainloop()