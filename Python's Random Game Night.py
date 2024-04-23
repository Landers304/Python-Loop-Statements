#Task 1:


import random

items = ["Baseball", "Football", "Glove", "Helmet", "Cleats"]

selected_item = random.choice(items)

guess = input("Guess which item was selected from the list: ")

if guess == selected_item:
    print("Correct! You made the right choice.")
else:
    print(f"Sorry, the correct item was {selected_item}. Better luck next time!")

