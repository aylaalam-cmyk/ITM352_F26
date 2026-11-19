import json
import time
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

# Each question has 30 seconds
QUESTION_TIME_LIMIT = 30

with Path(__file__).with_name("questions.json").open(encoding="utf-8") as file:
    questions = json.load(file)

question_items = list(questions.items())
max_questions = len(question_items)

score = 0
question_number = 0
quiz_results = []
current_feedback = None
hint_used = False
current_hint = None
question_deadline = None 
quiz_timed_out = False 

app = Flask(__name__, template_folder=".")

#home page and quiz reset
@app.route("/")
def index(): #runs and resets app before displaying
    global score, question_number, quiz_results, current_feedback
    global question_deadline, quiz_timed_out
    global hint_used, current_hint
    score = 0
    question_number = 0
    quiz_results = []
    current_feedback = None
    hint_used = False
    current_hint = None
    question_deadline = None
    quiz_timed_out = False
    return render_template("index.html")


#body of the app kinda
#shows the question, hint, answers, and moving to the next question
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, question_number, quiz_results, current_feedback, question_deadline
    global quiz_timed_out
    global hint_used, current_hint

    #timed out part and returns page
    if quiz_timed_out or question_number >= max_questions:
        return redirect(url_for("results"))

    # Start the 30 second timer/limit when question is shown
    if current_feedback is None and question_deadline is None:
        question_deadline = time.monotonic() + QUESTION_TIME_LIMIT

    #hint part of the button, shows hint, marks if hint has been used, reloads page if hint is used
    if request.method == "POST":
        if request.form.get("action") == "hint" and current_feedback is None:
            #a hint cn be used once but does not reset the timer
            if not hint_used and time.monotonic() < question_deadline:
                current_hint = question_items[question_number][1]["hint"]
                hint_used = True
            return redirect(url_for("quiz"))

        #Next button
            #clears previous question and loads next one or result page
        if request.form.get("action") == "next":
            question_number += 1
            current_feedback = None
            current_hint = None
            question_deadline = None
            if question_number >= max_questions:
                return redirect(url_for("results"))
            return redirect(url_for("quiz"))

        #checks that time isnt over, checks answer, and scores it if correct 
        if current_feedback is None:
            question, question_data = question_items[question_number]
            timed_out = time.monotonic() >= question_deadline #Reject answersif timed put
            selected_answers = (
                [] if timed_out else request.form.getlist("answer")
            )
            correct_answers = question_data["answers"][:2]
            is_correct = not timed_out and bool( # Count the question correct when either correct choice is selected
                set(selected_answers).intersection(correct_answers)
            )

            if is_correct:
                score += 1

            #saves feedback
            current_feedback = {
                "selected_answers": selected_answers,
                "correct_answers": correct_answers,
                "explanation": question_data["correct_response"],
                "is_correct": is_correct,
                "timed_out": timed_out,
            }
            #creates current score
            # adds current score to most recent answered question result
            quiz_results.append({
                "question": question,
                **current_feedback,
            })
            #end quiz when timed out
            if timed_out:
                quiz_timed_out = True
                return redirect(url_for("results"))

    #values
    return render_template(
        "quiz.html",
        question=question_items[question_number][0],
        question_number=question_number + 1,
        options=question_items[question_number][1]["answers"],
        score=score,
        questions_answered=len(quiz_results),
        feedback=current_feedback,
        hint=current_hint,
        hint_available=not hint_used,
        #remaining time displayed for countdown
        seconds_remaining=(
            max(0, int(question_deadline - time.monotonic() + 0.999))
            if current_feedback is None and question_deadline is not None
            else 0
        ),
    )

#maps and displays results 
#values
@app.route("/results")
def results():
    return render_template(
        "result.html",
        score=score,
        total_questions=max_questions,
        quiz_results=quiz_results,
        quiz_timed_out=quiz_timed_out,
    )

#atart website
if __name__ == "__main__":
    app.run(debug=True)#helps show errors