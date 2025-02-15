from data import question_data
from question_model import Question

questions = question_data

question_bank = []

for question in questions:
    text=question["text"]
    answer=question["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

#input(question_bank[1].text) since it's constructed in a differentmodule
#This is the only way to be able to access the text. I think....


