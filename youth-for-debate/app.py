from flask import Flask, render_template, jsonify
import pandas as pd
from update_tickets import update_tickets
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/raffle', methods=['GET'])
def raffle():
    # Update the CSV
    update_tickets()

    # Read in CSV
    df = pd.read_csv("ticket_tracker.csv")

    # Drop all columns except for tickets and student
    new_df = df[['tickets', 'student']]

    # Create list
    students_list = []
    for _, row in new_df.iterrows():
        students_list.extend([row['student']] * row['tickets'])

    # select winner
    winner = random.choice(students_list)
    return jsonify(winner=winner, students_list=students_list)

if __name__ == '__main__':
    app.run(debug=True)