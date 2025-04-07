# Equation Solver Game

## version 1.0

## Table of Contents

|Section| Subsection  |Description of Subsection|
|---|------------------------------|:-------------:|
|[User Guide](#user-guide)| Introduction    |  A brief overview of the user guide.  
|| Getting Started|  How to install and run the game.                     |   |
| |Playing The Game             | Instructions on how to play the game.            |
|[Technical Documentaion](#technical-documentation)| Project Overview| An outline of the game's purpose, requirements and architecture. |
| |Further Development | Ideas for developing the game's functionality.         |
|| License         |  Licensing and usage information.                
| |Conclusion| Final thoughts on the project.                      |
# User Guide

## Introduction
Welcome to the Equation Solver game! This programme is designed to help you practice your multiplication skills by finding the missing factor (X) for a series of questions. Please follow the guide below to get started. 

## Getting started

1. **Download and Installation**
    - Ensure you have python version 3 or higher installed on your system.
    - Python can be downloaded from the official website from the official website: [Python.org](https://www.python.org/downloads/).
    - No additional library are required for this programme to run.
    - Ensure you have the following two files installed:
      - game_logic.py
      - equation_solver.py
   - These should both be saved within the same folder. 
2. **Running the Programme from the console**
   - Open a terminal or command prompt on your computer.
   - Navigate to the folder where the programme files are saved. You can do this by inputting `cd` followed by the folder's path. 
   - Type the following command and press Enter:
     ```
     python equation_solver.py
     ```
    
3. **Running the Programme from an IDE**
    - The programme can also be ran in an integrated development environment (IDE) such as VSCode.
    - To do this, open your chosen IDE and load equation_solver.py
    - Locate and click on the **Run** button in the IDE to run the programme.

## Playing the Game
  - The game tests your mathematical skills by asking you to solve the missing factor (X) in 10 equations.
  - Within the terminal, you will be given an equation and asked "What is X?". For example: "6 * X = 54. What is X?".
  - To answer the question, simply input your answer into the terminal and press **enter key**. In the example above, the correct answer is 9. The game will display whether your answer is correct after each attempt.
  - Please enter your guess using only the numbers on your keyboard (e.g 99), as other forms of input including text (e.g. ninety nine) are not permitted. 
  - After 10 questions have been answered, you will be presented with your final score. 
  - You can stop the game at any time by pressing **CTRL/Command + C** on your keyboard.
  - To play the game again, simply rerun the programme using either step 2 or 3 above. Good luck!

---
# Technical Documentation

## Project Overview
- This programme is a python-based game designed to help users practice their multiplication skills by generating random multiplication questions and asking users to find the missing factor.
- The programme is written in python and requires users to have Python version 3 or higher installed.
- The programme is written in a modular way, allowing the game's logic and user interface to be modified and tested independently of one another.
## Technologies Used 
- **Programming Language:** Python Version 3 or higher
- **Modules:** 
  - `random` (standard python library module)
  - `equation_solver.py` (custom module)
  - `game_logic.py` (custom module)

## Code Explanation by Module 
1. `random`:
  - This is a standard library module used to generate random integers for the multiplication questions. 
2. `equation_solver.py`:
  - This is the module that the user interacts with. It is also the file they are instructed to load to play the game. 
  - This module imports the `run_game`function from `game_logic.py` and calls this function when ran. 
  - This causes the game to run in the terminal. 
3. `game_logic.py`:
  - This module contains two functions:
    - `generate_equation()`:
      - Uses the random function to generate two random integers between 0-15 (inclusive). 
      - Multiplies these integers together.
      - Returns a tuple containing the values of these two integers and their product, known as `num_1`, `num_2`, and `answer` respectively.
    - `run_game()`:
      - Creates a variable called "score" and initialises it to 0.
      - Nests the game's question logic in a loop allowing ten unique questions to be displayed each time the user plays.
      - Calls `generate_equation()` and unpacks the tuple returned to assign `num_1`, `num_2`, and `answer`as local variables within `run_game()`.
      - Concatenates these variables with strings to create the question shown to the user following the format `str(num_1) + " * X =" + str(answer) + "." + "What is X?"`.
      - Prompts the user to enter an answer by concatenating `int`with the string `Your Answer:`. Assigns the users input to the variable `user_answer`.
      - Performs input validation by asking the user to enter a valid integer if they have not done so. Excepts `ValueError`, preventing the game from crashing in such cases. 
      - Assesses the accuracy of the user's answer by comparing `user_answer` with `num_2`. The game will display a message letting the user know whether or not their guess is correct.
      - If the user's guess is correct (ie `user_answer == num_2`), 1 point is added to their score. If they are incorrect, no points are added and the game will display the correct answer. 
      - Upon the loop's completion, the game will display a message detailing the user's total score. It will also give the user some feedback based on their score. For example, displaying "Fantastic Score - Well Done!" for score of 8 or above.

      - This concludes the game. Users can play again by rerunning the programme using instructions provided in this manual. 

## Further Development 
This section contains some aspects that can be developed further to enhance the game's functionality and user engagement.
- Allowing users to customise the game's difficulty by changing the number of questions asked or the range used in `generate_question`.
- Adding a timer element that tracks how long a user takes to solve the questions.
- Adding another score metric that calculates a users overall score based on questions answered correctly and time taken to solve the questions.
- Adding a feature where users can save and share their high scores.

## Licence
This game is free to use and modify, no licensing restrictions apply.

## Conclusion
The equation solver game is a fun, interactive way for users to practice their multiplication skills. This simple programme is designed to be accessible and engaging, but also has the scope to include even more engaging features and customisation in future builds!


