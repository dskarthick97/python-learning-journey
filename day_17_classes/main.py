""" Quiz Game """

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for que_data in question_data:
    text = que_data.get("text")
    answer = que_data.get("answer")
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
