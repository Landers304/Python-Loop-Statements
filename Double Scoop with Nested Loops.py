#Task 1:


import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Relaxed", "Anxious"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

times_of_day = ["Morning", "Afternoon", "Evening"]


for day in days_of_week:
    print(f"Mood tracker for {day}:")
    for time in times_of_day:
        
        random_mood = random.choice(moods)
        
        print(f"{time}: {random_mood}")
    
