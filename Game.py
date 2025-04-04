import random  # Importing random module to generate random numbers for questions

def generate_equation():
    """
    Generate a simple equation with two random integers between 0 and 15.

    Parameters:
        None.

    Returns:
        Tuple: A tuple that contains two random integers (num_1, num_2) and their product (answer).
    """

    num_1 = random.randint(0, 15)  # Generate a random integer between 0 and 15 for number one
    num_2 = random.randint(0, 15)  # Generate a random integer between 0 and 15 for number two 
    answer = num_1 * num_2 # multiply number one by number two
    return num_1, num_2, answer #return the above variables

# Main programme asking users to guess X
def run_game():
    """
    The function uses the generate_equation function to 10 simple equations.
    The user must solve each question by finding the missing factor (X) in num_1 * X = answer.
    The game provides feedback after each guess on whether or not the user's answer is correct.
    The user's total score is tracked and presented once the game is completed.

    Parameters:
        None. 
    
    Raises:
        ValueError: If the user's input is not a valid integer.

    Returns:
        None.

    
    """
    score = 0 # Set the initial score to 0

    # Generate 10 questions to be presented to the user
    for _ in range(10):
        num_1, num_2, answer = generate_equation()
        message = str(num_1) + " * X =" + str(answer) + "." + "What is X?"
        print(message)

        try: # Check if the user's input is an integer 
            user_answer = int(input("Your answer: "))
        except ValueError: # Ask the user to enter an integer if their input is a non-integer
            print ("Please enter a valid integer.") 
            continue
    
        # Determine how the programme will respond to a user's guess.
        if user_answer == num_2:
            print("Correct!")
            score += 1
        else:
            print ("Wrong. The correct answer was: " + str(num_2))
 
# Print the user's total score after the questions have been answered
    total_score = "Your score is: " + str(score) + " out of 10"
    print(total_score)



