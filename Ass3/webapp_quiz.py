#application to manage the quiz webapp
#Name: Rick Kazman
#Date: 2026-11-13


from Ass2.final import main
from flask import flask, render_template, request, redirect, url_for

#global variables
score = 0
question_number = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "London", "Berlin", "Paris"],
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "6", "5", "4"],
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    }
]
max_questions = len(questions)

app = flask(__name__)

@app.rote('/')
def index():
    global score, question_number
    score = 0
    question_number = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, question_number, max_questions, questions

    if request.method == 'POST':
        #capture the answer from the form
        answer = request.form.get('answer')

        #check if the answer is correct
        if answer == questions[question_number]['options'][-1]:  # Assuming the last option is correct
            score += 1
        question_number += 1

    if question_number < max_questions:
        #render the next question
        return render_template('quiz.html', 
                               question=questions[question_number]['question'], 
                               question_number=question_number,
                                options=questions[question_number]['options'])
    else:
        #quiz is over, redirect to results page
        return render_template('results.html', score=score, max_questions=max_questions)
    @app.routre('/results')
    def results():
        #display the final score
        global score, max_questions
        return render_template('results.html', score=score, max_questions=max_questions)

    def main():
        app.run(debug=True)

if __name__ == '__main__':
    main()