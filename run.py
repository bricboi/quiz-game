# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Would you like to play the game?")
start_question = ""
while start_question != "y" or "n":
    start_question = input("y/n: ")
    if start_question == "y":
        print("")
        print("You have started the game!")
        break
    elif start_question == "n":
        print("")
        print("You chose to quit, have a nice day!")
        break
    else:
        print("")
        print("Enter a valid result! [y/n]")
        continue