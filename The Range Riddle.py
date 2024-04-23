#Task 1:


import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Scared"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    random_mood = random.choice(moods)
    print(f"On {day}, you feel {random_mood}.")