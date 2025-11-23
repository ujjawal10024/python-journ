from datetime import datetime

print("=== Workout Tracker ===")

while True:
    exercise = input("Enter exercise name (or 'q' to quit): ")

    if exercise.lower() == "q":
        print("Workout session ended.")
        break
    reps = input("Enter reps/sets: ")
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    entry = f"{date} | {exercise} | {reps}\n"

    with open("workout_log.txt" , "a") as file:
        file.write(entry)

    print("Workout saved!")

    choice = input("Add more? (yes/no): ")

    if choice.lower() != "yes":
        print("Good job ")
        break  