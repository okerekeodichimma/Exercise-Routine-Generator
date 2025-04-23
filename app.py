from flask import Flask, render_template, request
from utils.workout_generator import generate_workout_plan
import json

app = Flask(__name__)

with open('data/exercises.json') as f:
    EXERCISES = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fitness_level = request.form['fitness_level']
        equipment = request.form.getlist('equipment')
        goal = request.form['goal']

        workout_plan = generate_workout_plan(
            fitness_level, equipment, goal, EXERCISES
        )
        return render_template('workout_plan.html', plan=workout_plan)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)