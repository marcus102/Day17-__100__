from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for itens in question_data:
    questions = itens["text"]
    answers = itens["answer"]
    new_data = Question(questions, answers)
    question_bank.append(new_data)
    
quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()