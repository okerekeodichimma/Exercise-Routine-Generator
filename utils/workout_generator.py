import random
from .progressive_overload import calculate_sets_reps

def generate_workout_plan(fitness_level, equipment, goal, exercises):
    days = ["Monday", "Tuesday", "Thursday", "Friday"]
    plan = {}
    equipment_set = set(equipment) | {"bodyweight"}

    pool = [ex for ex in exercises if ex['equipment'] in equipment_set]

    for day in days:
        daily = []
        groups = random.sample(
            ["chest", "back", "legs", "shoulders", "arms", "core"], 4
        )
        for grp in groups:
            choices = [ex for ex in pool if grp in ex['muscle_group']]
            if not choices:
                continue
            ex = random.choice(choices)
            sets, reps = calculate_sets_reps(fitness_level, goal)
            daily.append({
                "name": ex['name'],
                "sets": sets,
                "reps": reps,
                "demo": ex['demo']
            })
       
        plan[day] = {
            "warm_up": ["5 min light cardio", "dynamic stretches"],
            "exercises": daily,
            "cool_down": ["5-10 min static stretching"]
        }
    return plan