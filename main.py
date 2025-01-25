import functions

print("Gym Tracker Options: "
      "\n1. Add Exercise"
      "\n2. Log Workout"
      "\n3. View Progress"
      "\n4. Exit")

while True:

    options = int(input("\nChoose an option: "))

    match (options):
        case 1:
            exercise = input("Enter exercise name: ")
            print(f"Added exercise: {exercise.title()}")

            listOfExercises = functions.get_exercise()
            listOfExercises.append(exercise.title() + "\n")

            functions.write_exercise(listOfExercises)

        case 2:
            exercise = input("Enter exercise name: ")
            numOfSets = int(input("Enter number of sets: "))
            numOfReps = int(input("Enter number of reps: "))
            weightInKg = float(input("Enter weight in kg: "))

            output = f"Logged {numOfSets} sets of {numOfReps} reps at {weightInKg}kg for {exercise}"
            print(output)
            log_entry = f"{exercise}:{output}\n"

            # Append the log to the exercise file
            listOfExercises = functions.get_exercise()
            listOfExercises.append(log_entry)
            functions.write_exercise(listOfExercises)

        case 3:
            progress = functions.get_exercise()

            if not progress:
                print("No progress logged yet.")
            else:
                logs_by_exercise = {}
                for item in progress:
                    item.strip("\n")
                    if ":" in item:
                        exercise_name, log = item.split(":", 1)
                        if exercise_name not in logs_by_exercise:
                            logs_by_exercise[exercise_name] = []
                        logs_by_exercise[exercise_name].append(log)

                for exercise_name, logs in logs_by_exercise.items():
                    print(f"Progress for {exercise_name}: \n")
                    for index, item in enumerate(logs, start=1):
                        print(f"Session {index}: {log}\n")

        case 4:
            exit(0)

        case _:
            print("Invalid option. Please choose 1, 2, or 3.")
