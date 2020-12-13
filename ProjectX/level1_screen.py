from tkinter import *


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
        askquestion1()


def askquestion1():
    global questions, level1_screen, index, level1_button, right, number_of_questions

    if len(questions) == index + 1:
        Label(level1_screen, text="Thank you for answering the questions. " + str(right) + " of " + str(
            number_of_questions) + " questions answered right").pack()
        return

    index += 1
    questions[index].getview(level1_screen).pack()



def level1():
    global level1_screen
    level1_screen = Tk()
    level1_screen.geometry("600x500")
    level1_screen.title("Level 1")
    askquestion1()

    level1_screen.mainloop()
