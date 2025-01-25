def get_exercise(filepath="exercises.txt"):
    with open(filepath, 'r') as file_local:
        exercise_local = file_local.readlines()
    return exercise_local

def write_exercise(exer_arg, filepath="exercises.txt"):
    with open(filepath, 'w') as file:
        file.writelines(exer_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_exercise())