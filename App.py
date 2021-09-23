# Written by K. M. Knausgård 2021-09-23
import random
import itertools

max_number_of_exercises = 100


def input_integer_number(message):
    while True:
        try:
            return int(input(message))
        except: pass


def main():
    print("Python Multiplication Table Learner 1.0\n")

    message = "Select number of exercises, maximum {}:   ".format(max_number_of_exercises)
    number_of_exercises = min(input_integer_number(message), max_number_of_exercises)
    print("\n  Ready!")

    exercises = list(itertools.product(range(0, 10), repeat=2))
    random.shuffle(exercises)

    for ii, exercise in enumerate(exercises[:number_of_exercises]):
        print("\n  Exercise number {} of {}:".format(ii+1, number_of_exercises))
        answer = input_integer_number("    {} x {} = ".format(exercise[0], exercise[1]))
        while answer != (exercise[0] * exercise[1]):
            print("    Wrong!")
            answer = input_integer_number("    {} x {} = ".format(exercise[0], exercise[1]))
        print("    CORRECT!")


if __name__ == "__main__":
    main()
