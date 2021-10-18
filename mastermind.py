import random


def generate_code():
    """
    Generates a list of 4 random integers between 1 and 8.
    It uses random.randint() for testing purposes
    """
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. \
Digits in range 1 to 8. You have 12 turns to break it.')
    return code
    

def check_input(answer):
    """
    Checks if the answer given has a length of 4
    """
    return len(answer) != 4


def get_input():
    """
    Recursively asks for input until a good input is received
    """
    answer = input("Input 4 digit code: ")
    if check_input(answer):
        print("Please enter exactly 4 digits.")
        return get_input()
    else:
        return answer


def check_answer(answer, code):
    """
    Checks answer against code,
    prints the number of correct digits
    in and not in the correct place.
    returns a boolean that checks
    if its correct or not
    """
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    print(
        'Number of correct digits in correct place:     '+
        str(correct_digits_and_position))
    print(
        'Number of correct digits not in correct place: '+
        str(correct_digits_only))
    return correct_digits_and_position == 4
    

# TODO: Decompose into functions
def run_game():
    """
    Starts a game of mastermind in the terminal
    """
    code = generate_code()
    #print(code)
    turns = 0
    while turns < 12:
        answer = get_input()
        turns += 1
        if check_answer(answer, code):
            print('Congratulations! You are a codebreaker!')
            break
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))


if __name__ == "__main__":
    """
    Starts the program
    """
    run_game()
