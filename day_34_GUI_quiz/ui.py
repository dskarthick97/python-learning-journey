""" Quiz Game Interface """

import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score card
        self.score = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        # canvas
        self.canvas = tkinter.Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Something", font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        self.true_image  = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(
            image=self.true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_image  = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(
            image=self.false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=que_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Reached the end of quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        res = self.quiz.check_answer("True")
        self.give_feedback(res)

    def false_pressed(self):
        res = self.quiz.check_answer("False")
        self.give_feedback(res)

    def give_feedback(self, is_right):
        self.canvas.config(bg="green") if is_right else self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
