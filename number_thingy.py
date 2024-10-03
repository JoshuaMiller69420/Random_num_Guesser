import random


def target(min, max):
    return random.randint(0,100)


def get_integer_input():
    pass


def computer():
    while computer != (min, max):
        while True:
            pass

def get_number_from_user(prompt):
    """prompts the user with the given prompt and returns a number"""
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Invalid input")
            
    return num

def player_turn(min, max, target):
    while True:
        guess = get_number_from_user(f"enter a number between {min} and {max} ")
        if guess > target:
            print("Guess is to high")
        elif guess < target:
            print("Guess is to low")
        elif guess == target:
            print("You got it correct!")
            break
            guess_count = 0
    #loop prompting the user to enter a number between min and max. 
    #increase guess_count on each guess. 
    #provide feedback on each guess, and return guess_count when they get it. 
    

    #stub
    return 5


def play():
    min = 0
    max = 100
    target_num = target(min, max)
    #see how many guesses it takes for the user to guess the nubmer
    user_guesses = player_turn(min, max, target_num)
    print(f"good job. you got it in {user_guesses}")


if __name__ == "__main__":
    play()