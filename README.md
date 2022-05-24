# SmashSudoku 

## Table of Contents 
- <a href="#about">About SmashSudoku</a>
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

# About SmashSudoku
SmashSudoku is a Python terminal game. It is deployed on Heroku and uses a mock terminal custom made by Code institute. 

Users can play the classic game of Sudoku popularised by Maki Kaji.

Users can select an easy, medium or hard Sudoku puzzle to solve,  and after finishing the puzzle users can see the correct solution. 

[The deployed site is here!](https://smashed-sudoku.herokuapp.com/)

<img src="assets/images/smashsami.jpeg">

</section>
<section id="how_to">

# How to play 

SmashSudoku is based on the classic pen and paper game Sudoku, popularised by Maki Kanji. You can learn more about Sudoku [here](https://en.wikipedia.org/wiki/Sudoku)

The rules for Sudoku are as follows -

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
-  As a user I want to know if my solution is correct or not.
- As a user I want to be able to pencil in numbers that can be edited later.


All user needs are met by the program. 

  - It is fully digital. 

  - It has 3 levels of difficulty to choose from. 

  - The user can choose to see the solution at the end of the game. 


  ## <p id="typography">Typography</p> 

  - [Arial](https://docs.microsoft.com/en-us/typography/font-list/arial) is used for the "RUN PROGRAM" button. 

</section>

<section id="features">

## <p id="solution">Solution</p>
- When user has finished filling the board they can choose to see the solution to the board. If the user wants to leave the game they can input number 10 and the solved puzzle will be presented on screen.


<img src="assets/images/solution.png">


## <p id="input_val">Input Validation</p>

- Difficulty selection
  - You can not select anything other than 1, 2 or 3

<img src="assets/images/dif_input.png">

- Row, Column input 
  - You can only input a number(1-9) for each row and column.
  - 

<img src="assets/images/r_c_input.png">

- Number Input 
  - You can only input number (1-9)

<img src="assets/images/num_h_input.png">

- See solution & play again input
  - You can only enter '10'

<img src="assets/images/y_n_input.png">

## <p id="future">Future Features</p>
- implement app into a GUI like pygame
- add a timer

</section>


