from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


questions = question_data

question_bank = []

for question in questions:
    text=question["text"]
    answer=question["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)


for x in range(1,12):
    answer = input(f"Q.{x}.{question_bank[x].text}[True/False]: ")
    if answer == question_bank[x].answer:
        print("Correct!")
    elif answer != question_bank[x].answer:
        print("WRONG!!")


#input(question_bank[1].text) since it's constructed in a differentmodule
#This is the only way to be able to access the text. I think....


