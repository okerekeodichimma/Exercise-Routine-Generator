import random

def calculate_sets_reps(fitness_level, goal):
    sets_map = {"beginner": 3, "intermediate": 4, "advanced": 5}
    sets = sets_map.get(fitness_level, 3)

    if goal == "strength":
        reps = random.randint(4, 6)
    elif goal == "hypertrophy":
        reps = random.randint(8, 12)
    elif goal == "fat_loss":
        reps = random.randint(12, 20)
    else:
        reps = random.randint(8, 12)

    return sets, reps