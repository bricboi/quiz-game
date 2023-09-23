import random
# list for the questions in the game
random_order = []
game_list = []
user_answers = []


def get_question_list():
    """
    Ceates a list of questions and answers to be used in the game
    """
    question_answer_list = [
        {
            "question": "How many days are in a year?",
            "1": "31 days",
            "2": "400 days",
            "3 x": "365 days",
            "4": "12 days"
        },
        {
            "question": "What fruit is round and orange?",
            "1": "Pear",
            "2": "Banana",
            "3": "Apple",
            "4 x": "Orange"
        },
        {
            "question": "What is the answer to the ultimate question of life the universe and everything?",
            "1 x": "42",
            "2": "Pizza",
            "3": "3.1415926535...",
            "4": "Chocolate"
        },
        {
            "question": "What is the capital of Australia?",
            "1": "New York",
            "2": "Ottawa",
            "3": "Sydney",
            "4 x": "Canberra"
        },
        {
            "question": 'Who wrote the novel "1984"?',
            "1": "J.R.R Tolkein",
            "2 x": "George Orwell",
            "3": "Agatha Christie",
            "4": "Dr. Seuss"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "1": "H2O",
            "2": "C",
            "3 x": "Au",
            "4": "Go"
        },
        {
            "question": "What year did the Titanic sink?",
            "1": "1999",
            "2 x": "1912",
            "3": "1876",
            "4": "1997"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "1": "Pluto",
            "2": "Earth",
            "3": "The sun",
            "4 x": "Jupiter"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "1 x": "Leonardo da Vinci",
            "2": "Leonardo DiCaprio",
            "3": "Vincent van Gogh",
            "4": "Michelangelo"
        },
        {
            "question": "What is the tallest mountain in the world?",
            "1": "K2",
            "2": "Kilimanjaro",
            "3 x": "Mount Everest",
            "4": "Fuji"
        },
        {
            "question": "What is the largest mammal in the world?",
            "1": "An elephant",
            "2": "A giraffe",
            "3 x": "The blue whale",
            "4": "An ostrich"
        },
        {
            "question": 'Who wrote the play "Romeo and Juliet"?',
            "1": "M. Night Shyamalan",
            "2 x": "William Shakespeare",
            "3": "Lin-Manuel Miranda",
            "4": "Sofokles"
        },
        {
            "question": "What gas do plants absorb from the atmosphere and use in photosynthesis?",
            "1": "Water (H2O)",
            "2": "Oxygen (O)",
            "3 x": "Carbon dioxide (CO2)",
            "4": "Hydrogen (H)"
        },
        {
            "question": "What is the capital of Brazil?",
            "1 x": "Brasilia",
            "2": "Sao Paulo",
            "3": "Rio de Janeiro",
            "4": "Salvador"
        },
        {
            "question": "What is the chemical symbol for iron?",
            "1": "Ir",
            "2": "Cl",
            "3": "Au",
            "4 x": "Fe"
        },
        {
            "question": "Who was the first woman to fly solo across the Atlantic Ocean?",
            "1 x": "Amelia Earhart",
            "2": "Jane Austen",
            "3": "Catherine the Great",
            "4": "Marie Curie"
        },
        {
            "question": "What is the largest organ in the human body?",
            "1": "The liver",
            "2 x": "The skin",
            "3": "The brain",
            "4": "The heart"
        },
        {
            "question": 'Which planet is known as the "Red Planet"?',
            "1": "Jupiter",
            "2": "Mercury",
            "3": "Venus",
            "4 x": "Mars"
        },
        {
            "question": 'Who is the author of "To Kill a Mockingbird"?',
            "1 x": "Harper Lee",
            "2": "Jane Austen",
            "3": "J.R.R Tolkein",
            "4": "J.K. Rowling"
        },
        {
            "question": "What is the capital of England?",
            "1": "Liverpool",
            "2": "Birmingham",
            "3 x": "London",
            "4": "Oxford"
        }
    ]
    return question_answer_list


def print_dictionary():
    """
    (TEST) Prints the dictionary questions and answers to the console
    """
    # get the question list
    for x in range(len(get_question_list())):
        " Define dictionary "
        dictionary = get_question_list()[x]
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
        start_question = start_question.strip()
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
    Selects ten random questions from the list and adds them to the game_list
    """
    x = 0
    while x != 10:
        # get a random number based on the length of the question list
        random_num = random.randint(0, len(get_question_list()) - 1)
        # checks if there is repetition and pervents it
        if len(random_order) == 0:
            random_order.append(random_num)
            x += 1
        elif random_num in random_order:
            continue
        elif x == 10:
            x = 10
            break
        else:
            random_order.append(random_num)
            x += 1
        # add the question to the games and question list
    for i in random_order:
        dictionary = get_question_list()[i]
        game_list.append(dictionary)
    write_question()


def write_question():
    """
    Prints a question and asks for input
    """
    # write 10 questions that require user input
    for x in range(10):
        answer_loop = 0
        value = list(game_list[x].values())
        print(f"\nQuestion {x + 1}: {value[0]}\n")
        print(f"1: {value[1]}")
        print(f"2: {value[2]}")
        print(f"3: {value[3]}")
        print(f"4: {value[4]}\n")
        # Check if answer is 1, 2, 3 or 4 else invalid answer
        while answer_loop != 1:
            answer = input("Answer:")
            answer = answer.strip()
            if answer == "1":
                user_answers.append(answer)
                answer_loop = 1
            elif answer == "2":
                user_answers.append(answer)
                answer_loop = 1
            elif answer == "3":
                user_answers.append(answer)
                answer_loop = 1
            elif answer == "4":
                user_answers.append(answer)
                answer_loop = 1
            else:
                print("Enter a valid answer (1, 2, 3, 4)")
                continue
    check_if_correct()


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
