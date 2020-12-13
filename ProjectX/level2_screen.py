from tkinter import *


class Question:
    def __init__(self, question, answers, correctLetter):
        print('question object is created')
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        print('check')
        global right
        if letter == self.correctLetter:
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackview(view))

    def getview(self, appwindow):
        print('get_view')
        view = Frame(appwindow)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackview(self, view):
        print('unpack_view')
        view.pack_forget()
        askquestion2(questions)


def askquestion2(questions):
    print('askquestion2')
    global level2_screen, index, level1_button, right, number_of_questions

    if len(questions) == index + 1:
        Label(level2_screen, text="Thank you for answering the questions. " + str(right) + " of " + str(
            number_of_questions) + " questions answered right").pack()
        return

    index += 1
    questions[index].getview(level2_screen).pack()



def level2(questions):
    print('level2')
    global level2_screen
    level2_screen = Tk()
    level2_screen.geometry("600x500")
    level2_screen.title("Level 2")
    askquestion2(questions)

    level2_screen.mainloop()