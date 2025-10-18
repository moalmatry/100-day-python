from data import question_data
from utils import generate_questions
from quiz_brain import QuizBrain

question_bank = generate_questions(question_data)

quiz = QuizBrain(question_bank)
quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()
