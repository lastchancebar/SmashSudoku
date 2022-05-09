# Smashing Sudoku 

## Table of Contents 
- <a href="#about">About Smashing Sudoku</a>
- <a href="#how_to">How to play</a>
- <a href="#ux">UX Design</a>
  - <a href="#user_stories">User Stories</a>
  - <a href="#typography">Typography</a>
  - <a href="#color">Color</a>
- <a href="#features">Features</a>
  - <a href="#difficulty">Difficulty Settings</a>
  - <a href="#board">Board</a>
  - <a href="#input">Colored Input</a>
  - <a href="#rules">Rules</a>
  - <a href="#val_check">Validity Check</a>
  - <a href="#timer">Timer</a>
  - <a href="#solution">Solution</a>
  - <a href="#play_again">Play Again</a>
  - <a href="#input_val">Input Validation</a>
  - <a href="#future">Future Features</a>
- <a href="#data_model">Data Model</a>
  - <a href="#attributes">Attributes</a>
  - <a href="#methods">Methods</a>
- <a href="#logic">Logic flow</a>
- <a href="#techno">Technologies Used</a>
- <a href="#testing">Testing</a>
  - <a href="#bugs">Bugs</a>
  - <a href="#validator_test">Validator Testing</a>
  - <a href="#test_user_stories">Testing User Stories</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
  - <a href="#tutorials">Tutorials</a>
  - <a href="#acknowledgements">Acknowledgements</a>

<section id="about">

# About Smashing Sudoku
Smashing Sudoku is a Python terminal game. It is deployed on heroku and uses a mock terminal made by Code institute. 

Users can play the classic game of Sudoku popularised by Maki Kaji.

Users can select an easy, medium or hard Sudoku puzzle to solve, get hints if they are stuck on a square, and after finishing the puzzle users can see the correct solution as well as see how long it took to fill the board. 

[The deployed site is here!](https://smashing-sudoku.herokuapp.com/)

<img src="assets/images/am-i-responsive.png">

</section>
<section id="how_to">

# How to play 

Smashing Sudoku is based on the classic pen and paper game Sudoku, popularised by Maki Kanji. You can learn more about Sudoku [here](https://en.wikipedia.org/wiki/Sudoku)

The rules for Sudoku are quite simple. 

- There is a 9 x 9 grid which must be filled with numbers
- The game starts with some squares already filled in
- only the numbers 1 - 9 can be used 
- Every square must contain one number 
- Each 3×3 box can only contain each number from 1 to 9 once
- Each vertical column can only contain each number from 1 to 9 once
- Each horizontal row can only contain each number from 1 to 9 once

</section>

<section id="ux">

# UX Design

## <p id="user_stories"> User Stories</p>
- As a user I want a digital version of sudoku to avoid paper waste.
- As a user I want varying levels of difficulty to suit the mood I am in or to train myself to get better at sudoku. 
- As a user I want the option to get hints to the correct solution whenever I need it. 
- As a user I want to know if my solution is correct or not.
- As a user I want to be able to pencil in numbers that can be edited later.
- As a user, I want to know how long it takes me to complete a puzzle.

All user needs are met by the program. 

  - It is fully digital. 

  - It has 3 levels of difficulty to choose from. 

  - The user can get hints to any cell on the board. 

  - The user can choose to see the solution at the end of the game. 

  - The user inputs in red can be re-inputted.

  - A timer displays how long it took to complete the game at the end of the game. 

  ## <p id="typography">Typography</p> 

  - [Arial](https://docs.microsoft.com/en-us/typography/font-list/arial) is used for the "RUN PROGRAM" button. 


