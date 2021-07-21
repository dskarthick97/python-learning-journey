""" Quiz Brain """


class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        length_of_question_list = len(self.question_list)
        return self.question_number < length_of_question_list

    def next_question(self):
        """ 
        Retrieves the item at the current question number from the question list.
        """
        question = self.question_list[self.question_number]
        text = question.text
        self.question_number += 1
        res = input(f"Q.{self.question_number}: {text} (True/False)?: ")
        self.check_answer(res, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
