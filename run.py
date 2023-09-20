question_answer_list = [
    {
        "question": "how many days are in a year? (not counting leap years)",
        "1": "31 days",
        "2": "400 days",
        "3": "365 days x",
        "4": "12 days"
    },
    {
        "question": "what fruit is round and orange?",
        "1": "Pear",
        "2": "Banana",
        "3": "Apple",
        "4": "Orange x"
    },
    {
        "question": "what is the answer to the ultimate question of life the universe and everything?",
        "1": "Cheese",
        "2": "42 x",
        "3": "Pasta",
        "4": "21"
    },
]


def print_dictionary():
    """
    (TEST) Prints the dictionary questions and answers to the console
    """
    for x in range(len(question_answer_list)):
        " Define dictionary "
        dictionary = question_answer_list[x]
        print(f"Question #{x + 1}")
        for question, answer in dictionary.items():
            print(f"{question}: {answer}")
        print("\n")


def start_game():
    """
    Asks the user if they wish to start a new game
    """
    print("Would you like to play the game? y=yes n=no")
    start_question = ""
    while start_question != "y" or "n":
        start_question = input("[y/n]: ").lower()
        if start_question == "y":
            print("\nStarting game!")
            select_random_question()
            break
        elif start_question == "n":
            print("\nYou chose to quit, have a nice day!")
            break
        elif start_question == "print":
            print_dictionary()
        else:
            print("\nEnter a valid result! [y/n]")
            continue


def select_random_question():
    """
    Selects a random question from the list
    """
    print("Selecting random question!")


def write_question():
    """
    Prints a question and asks for input
    """
    print("Is this a question?")


def check_if_correct():
    """
    Checks if the answer is correct
    """
    print("Checking if the answer is correct")


def calculate_result():
    """
    Calculates the result and adds to score
    """
    print("calculating! score is still 0!")


start_game()
