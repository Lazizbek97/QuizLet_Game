from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizLetUI():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("QuizLet")
        self.window.configure(background = THEME_COLOR)
        self.score = 0



        self.canva = Canvas(width = 300, height=250, bg="white")
        self.question_text = self.canva.create_text(150, 125,text = "quiz go here", width = 280, font=("Arial", 20, "italic"))
        self.canva.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text = f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 15, "italic"), fg="white")
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.true_image = PhotoImage(file = "images/true.png")
        self.true_but = Button(image=self.true_image, highlightthickness=0, command=self.right_answer)
        self.true_but.grid(column=0, row=2, padx=20, pady=20)

        self.x_image = PhotoImage(file="images/false.png")
        self.x_but = Button(image=self.x_image, highlightthickness=0, command=self.wrong_answer)
        self.x_but.grid(column=1, row=2, padx=20, pady=20)

        self.next_quiz()
        self.window.mainloop()
    def next_quiz(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")

            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text,text = q_text)
        else:
            self.canva.itemconfig(self.question_text,text = "You've answered all questions!")
            self.true_but.config(state="disabled")
            self.x_but.config(state="disabled")

    def right_answer(self):
        is_true = self.quiz.check_answer("True")
        if is_true:
            self.canva.config(bg="green")
            self.score += 1
        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.next_quiz)

    def wrong_answer(self):
        is_false = self.quiz.check_answer("False")
        if is_false:
            self.canva.config(bg="green")
            self.score += 1

        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.next_quiz)

