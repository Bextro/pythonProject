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
        askquestionlevel1(b)


def askquestionlevel1(b):
    global questions, window, index, right, number_of_questions

    if len(questions) == index + 1:
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(
            number_of_questions) + " questions answered right").pack()
        return
    b.pack_forget()
    index += 1
    questions[index].getview(window).pack()


questions = []
file = open("level1questions.txt", "r")
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

