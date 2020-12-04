from quiz_app.level1 import askquestionlevel1
from tkinter import *
import os

# ------------------------------------------------------------------------------------------------------
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if letter == self.correctLetter:
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackview(view))

    def getview(self, appwindow):
        view = Frame(appwindow)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackview(self, view):
        view.pack_forget()
        askquestionlevel2()


def askquestionlevel2():
    global questions, window, index, level2_b, right, number_of_questions

    if len(questions) == index + 1:
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(
            number_of_questions) + " questions answered right").pack()
        return
    level2_b.pack_forget()
    level1_b.pack_forget()
    index += 1
    questions[index].getview(window).pack()


questions = []
file = open("level2.txt", "r")
line = file.readline()
while line != "":
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)


# ---------------------------------------------------------------------------------------------------------
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("600x500")

    global username
    global password
    global firstname
    global lastname
    global id
    global contactno
    global city
    global state
    global username_entry
    global password_entry
    global firstname_entry
    global lastname_entry
    global id_entry
    global contactno_entry
    global city_entry
    global state_entry

    username = StringVar()
    password = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    id = StringVar()
    contactno = StringVar()
    city = StringVar()
    state = StringVar()

    Label(register_screen, text="Please enter details below", bg="yellow").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username : ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password : ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    firstname_lable = Label(register_screen, text="FirstName : ")
    firstname_lable.pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()

    lastname_lable = Label(register_screen, text="LastName : ")
    lastname_lable.pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()

    id_lable = Label(register_screen, text="ID : ")
    id_lable.pack()
    id_entry = Entry(register_screen, textvariable=id)
    id_entry.pack()

    contactno_lable = Label(register_screen, text="ContactNo : ")
    contactno_lable.pack()
    contactno_entry = Entry(register_screen, textvariable=contactno)
    contactno_entry.pack()

    city_lable = Label(register_screen, text="City : ")
    city_lable.pack()
    city_entry = Entry(register_screen, textvariable=city)
    city_entry.pack()

    state_lable = Label(register_screen, text="State : ")
    state_lable.pack()
    state_entry = Entry(register_screen, textvariable=state)
    state_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="pink", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="If you have the login enter the login if u dont have the login press egister button").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username : ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password : ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    id_info = id.get()
    contactno_info = contactno.get()
    city_info = city.get()
    state_info = state.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(firstname_info + "\n")
    file.write(lastname_info + "\n")
    file.write(id_info + "\n")
    file.write(contactno_info + "\n")
    file.write(city_info + "\n")
    file.write(state_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# ---------------------------------------------------------------------------------------------------------
def dangit():
    global window,level2_b,level1_b
    main_screen.destroy()
    window = Tk()
    window.geometry('600x400')
    window.title("Quiz app")
    level1_b = Button(text="Level 1", height="2", width="30", command=askquestionlevel1)
    level1_b.pack()
    Label(text="").pack()
    level2_b = Button(text="Level 2", height="2", width="30", command=askquestionlevel2)
    level2_b.pack()
    Label(text="").pack()



def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Quiz app")
    main_label = Label(text="Want to start ?", bg="green", width="300", height="2", font=("Calibri", 13))
    main_label.pack()
    Label(text="").pack()
    login_button = Button(text="|LOGIN|", height="2", width="30", command=login)
    login_button.pack()
    Label(text="").pack()
    register_button = Button(text="|REGISTER|", height="2", width="30", command=register)
    register_button.pack()
    Label(text="").pack()
    start_button = Button(text="|START|", height="2", width="30", command=dangit)
    start_button.pack()
    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()
