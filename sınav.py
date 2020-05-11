class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0

q1 = Question('en iyi programlama dili hangisidir?',['C','c#','python'],'python')
q2 = Question('en popüler programlama dili hangisidir?',['C','python','c#'],'python')
q3 = Question('en çok kazandıran programlama dili hangisidir?',['c#','python','C'],'python')
questions = [q1,q2,q3]
quiz = Quiz(questions)

question = quiz.questions[quiz.questionsIndex]
print(question.text)
"""
print(q1.checkAnswer('C'))
print(q2.checkAnswer('python'))
"""
