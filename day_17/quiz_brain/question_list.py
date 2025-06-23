import random

from quiz_data import quiz_data

class Question:

    def __init__(self, q_text, q_answer):
        self.number = 0
        self.text = q_text
        self.answer = q_answer

class QuestionList:

    def __init__(self):
        self.number_of_questions = 10
        self.questions = []
        self.initialize_questions()

    def initialize_questions(self):
        random_list = random.sample(quiz_data, self.number_of_questions)
        for random_question in random_list:
            question = Question(random_question["question"], random_question["correct_answer"])
            self.questions.append(question)
