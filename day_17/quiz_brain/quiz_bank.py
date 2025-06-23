from day_17.quiz_brain.question_list import QuestionList


class QuizBank:

    def __init__(self, question_list: QuestionList):
        self.score = 0
        self.questions = question_list
        self.question_number = 0

    def next_question(self):
        question = self.questions.get_question_by_index(self.question_number)
        self.question_number += 1
        answer = input(f"Q.{self.question_number}. {question.text} (True/False): ").lower()

        if answer == question.answer.lower():
            print("You've got it right!")
            self.score += 1
        else:
            print("You got it wrong.")

        print(f"Current score: {self.score} / {self.question_number}\n")

    def still_have_questions(self):
        return self.question_number < self.questions.number_of_questions

    def start_quiz(self):
        while self.still_have_questions():
            self.next_question()

        print(f"End of quiz.")
        print(f"Your final score is {self.score} out of {self.questions.number_of_questions}")

