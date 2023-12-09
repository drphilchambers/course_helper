# Created by Phil Chambers, 2023, phil@philipchambers.dev

"""
Creates a connection between a local privateGPT "primordial" instance 
and a web interface for the purposes of embedding a chatbot inside
a Learning Management System such as Canvas pages.
"""

import subprocess
import sys
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
messages = []


@app.route("/")
def index():
    return render_template("index.html", messages=messages)


@app.route("/answer", methods=["POST"])
def get_answer():
    user_question = request.json["question"]
    program_answer = get_program_answer(user_question)
    messages.append({"user": user_question, "answer": program_answer})
    return jsonify({"answer": program_answer})


def get_program_answer(user_question):
    result = subprocess.run(
        [sys.executable, "privateGPT.py", "-S"],
        input=user_question,
        capture_output=True,
        text=True,
    )
    program_output = result.stdout

    answer_start_index = program_output.rfind("> Answer:")
    if answer_start_index != -1:
        answer_start_index += len("> Answer:")
        answer = program_output[answer_start_index:].strip()
        # Remove trailing "Enter a query:" if present
        enter_query_index = answer.rfind("Enter a query:")
        if enter_query_index != -1:
            answer = answer[:enter_query_index].strip()
    else:
        answer = ""

    return answer


if __name__ == "__main__":
    app.run()
