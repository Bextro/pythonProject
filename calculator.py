from tkinter import *


def multiply():
    try:
        label.config(text=float(first_entry.get()) * float(second_entry.get()))
    except ValueError:
        label.config(text='Enter valid numbers', font='Arial 8 bold')


def divide():
    try:
        label.config(text=float(first_entry.get()) / float(second_entry.get()))
    except ZeroDivisionError:
        label.config(text='There is no zero division', font='Arial 8 bold')
    except ValueError:
        label.config(text='Enter valid numbers', font='Arial 8 bold')


def total():
    try:
        label.config(text=float(first_entry.get()) + float(second_entry.get()))
    except ValueError:
        label.config(text='Enter valid numbers', font='Arial 8 bold')


def deduction():
    try:
        label.config(text=float(first_entry.get()) - float(second_entry.get()))
    except ValueError:
        label.config(text='Enter valid numbers', font='Arial 8 bold')


def delete():
    first_entry.delete(0, END)
    second_entry.delete(0, END)


root_window = Tk()
root_window.title('Calculator')
root_window.geometry('300x250')
root_window.configure(background='beige')

label = Label(text='Calculator', font='Arial 16 bold')
label.config(bd=10)
label.pack()

first_entry = Entry(width=30)
first_entry.insert(0, 'Enter first number:')
first_entry.pack()

second_entry = Entry(width=30)
second_entry.insert(0, 'Enter second number:')
second_entry.pack()

multiplication_button = Button(text=' * ', bg='#F2D9F3', fg='#000000', width=10, height=1, command=multiply)
multiplication_button.pack()

divison_button = Button(text=' / ', bg='#F2D9F3', fg='#000000', width=10, height=1, command=divide)
divison_button.pack()

total_button = Button(text=' + ', bg='#F2D9F3', fg='#000000', width=10, height=1, command=total)
total_button.pack()

deduction_button = Button(text=' - ', bg='#F2D9F3', fg='#000000', width=10, height=1, command=deduction)
deduction_button.pack()

delete_button = Button(text='Delete', bg='#F2D9F3', fg='#000000', width=10, height=1, command=delete)
delete_button.pack()

label = Label(text='', font=('Arial', 16, 'bold'))
label.config(bd=10)
label.pack(side=LEFT)

root_window.mainloop()
