# Quiz_2_DAA_C_2022
Quiz 2 Design and Analysis of Algorithms (DAA) 2022 class C Institut Teknologi Sepuluh Nopember 20 April 2022 - 12 May 2022.

**Author:**

Hafizh Mufid Darusalam - 5025201093

# Design and Analysis of Algorithms
In this Quiz 2, we were tasked with making a computer program that implements any kind of algorithms we have learned in this course, such as BFS, DFS, Kruskal, DAG, and so on. With that in mind, we came up with the idea to make a computer program to play tic tac toe. 

![image](https://user-images.githubusercontent.com/79137636/168080525-546f075a-4a5d-4ad0-8ac3-235e0c935a03.png)

The algorithm we will implement is called the minimax algorithm which is quite similar to the breadth-first search (BFS). While breadth-first search is considered an uninformed search, the minimax is considered an informed search. 

![image](https://user-images.githubusercontent.com/79137636/168082893-e791ed82-f1c2-4241-922c-a9997fe90467.png)

One of the differences between uninformed and informed searches is how they work. In an uninformed search, the program doesn’t have any additional information other than what is already defined. It only knows about the start state and goal state, but any information regarding how to achieve the goal state is not included. That’s why an uninformed search can also be called a blind search. Breadth-first search, as one of the uninformed search algorithms, will explore every possibility to reach the goal. We can represent it as a tree of possibilities and when it reached the goal, the algorithm finishes. Even though it has reached the goal, because it didn’t have any additional information, it can be inefficient. The minimax on the other hand will calculate a specific value from different scenarios. This value then will be used to minimize the opponent’s possibility to win the game and maximize the computer’s possibility to win the game, thus named minimax.

![image](https://user-images.githubusercontent.com/79137636/168083017-49574b2a-2437-499d-bc0d-61a223feb302.png)

# Source Code
There are two source codes involved using pygame language namely main.py and tictactoe.py. main.py is used to run the game especially rendering the game window and enabling interaction between user and computer whereas tictactoe.py is used to store functions that is going to be used in the tic tac toe gameplay. Besides that, there is also a font file used for the game window interface.

**main.py**

```
import pygame
import sys
import time
import tictactoe as ttt
```
First, we will import libraries needed. In this case, pygame, sys, time, and tictactoe (tictactoe.py file) as ttt.
```
pygame.init();
size = width, height = 600, 400;

# Colors
black = (0, 0, 0);
white = (255, 255, 255);

screen = pygame.display.set_mode(size);

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28);
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40);
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60);
```
After that, we initialize the game window. We also determine its dimension, colours involved, and text involved along with the chosen font.
```
user = None;
board = ttt.initial_state();
ai_turn = False;
```
Then, we initialize the 3x3 grid as board.
```
while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit();

  screen.fill(black);

  # Let user choose a player, X or O
  if user is None:

    # Draw title
    title = largeFont.render("Play Tic Tac Toe", True, white);
    titleRect = title.get_rect();
    titleRect.center = ((width/2), 50);
    screen.blit(title, titleRect);

    # Draw buttons
    playXButton = pygame.Rect((width/8), (height/2), (width/4), 50);
    playX = mediumFont.render("Play as X", True, black);
    playXRect = playX.get_rect();
    playXRect.center = playXButton.center;
    pygame.draw.rect(screen, white, playXButton);
    screen.blit(playX, playXRect);
  
    playOButton = pygame.Rect((5*(width/8)), (height/2), (width/4), 50);
    playO = mediumFont.render("Play as O", True, black);
    playORect = playO.get_rect();
    playORect.center = playOButton.center;
    pygame.draw.rect(screen, white, playOButton);
    screen.blit(playO, playORect);
```
Then, we render the game window as well as the buttons involved.
```
    # Check if button is clicked
    click, _, _ = pygame.mouse.get_pressed();
    if click == 1:
      mouse = pygame.mouse.get_pos();
      if playXButton.collidepoint(mouse):
        time.sleep(0.2);
        user = ttt.X;
      elif playOButton.collidepoint(mouse):
        time.sleep(0.2);
        user = ttt.O;
```
We can let user choose which side to play: X or O. If user choose X, user will go first. If user choose O, computer will go first. So, in both cases, X always go first.
```
else:

    # Draw game board
    tile_size = 80;
    tile_origin = ((width/2 - (1.5*tile_size)), (height/2 -(1.5*tile_size)));
    tiles = [];

    for i in range(3):
      row = [];
      for j in range(3):
        rect = pygame.Rect(
          tile_origin[0] + j*tile_size,
          tile_origin[1] + i*tile_size,
          tile_size, tile_size
        )
        pygame.draw.rect(screen, white, rect, 3);
        if board[i][j] != ttt.EMPTY:
          move = moveFont.render(board[i][j], True, white);
          moveRect = move.get_rect();
          moveRect.center = rect.center;
          screen.blit(move, moveRect);  
        row.append(rect);
      tiles.append(row);
```
Drawing the board.
```
    game_over = ttt.terminal(board);
    player = ttt.player(board);

```
Checking whether the game has already over for game_over and deciding which player to go for player.
```
    # Show title
    if game_over:
      winner = ttt.winner(board);
      if winner is None:
        title = f"Game Over: Tie.";
      else:
        title = f"Game Over: {winner} wins."
    elif user == player:
      title = f"Play as {user}"
    else:
      title = f"Computer thinking..."
    title = largeFont.render(title, True, white);
    titleRect = title.get_rect();
    titleRect.center = ((width/2), 30);
    screen.blit(title, titleRect);
```
Rendering the title of the game window.
```
    # Check for AI move
    if user != player and not game_over:
      if ai_turn:
        time.sleep(0.5);
        if ttt.difficulty():
          move = ttt.minimax(board);  # Give the AI the optimal move        
        else:
          move = ttt.maximin(board); # Give the AI the suboptimal move
        board = ttt.results(board, move);
        ai_turn = False;
      else:
        ai_turn = True;
```
Computer or AI can take a move based on the current board situation. It will call the function minimax to find the optimal move or maximin to find the suboptimal move.
```
    # Check for a user move
    click, _, _ = pygame.mouse.get_pressed();
    if click == 1 and user == player and not game_over:
      mouse = pygame.mouse.get_pos();
      for i in range(3):
        for j in range(3):
          if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
            board = ttt.results(board, (i, j));
    if game_over:
      againButton = pygame.Rect(width/3, height-65, width/3, 50);
      again = mediumFont.render("Play again", True, black);
      againRect = again.get_rect();
      againRect.center = againButton.center;
      pygame.draw.rect(screen, white, againButton);
      screen.blit(again, againRect);
      click, _, _ = pygame.mouse.get_pressed();
      if click == 1:
        mouse = pygame.mouse.get_pos();
        if againButton.collidepoint(mouse):
          time.sleep(0.2);
          user = None;
          board = ttt.initial_state();
          ai_turn = False;
  pygame.display.flip();

```
User can choose what move to take and the board will be updated after user made the move.

**tictactoe.py**

```
import math
import copy
import random
```
First, we will import libraries needed. In this case: math, copy, and random.
```
X = "X";
O = "O";
EMPTY = None;
```
We will also initiate some variables.
```
def initial_state():
  """Returns the starting state of the board where all the 9 slots from the 3x3 board is empty."""
  
  return [[EMPTY, EMPTY, EMPTY], 
          [EMPTY, EMPTY, EMPTY], 
          [EMPTY, EMPTY, EMPTY]]
```
Function above will be used to return a starting state of the board.
```
def player(board):
  """Returns player who has the next turn on the board."""
  
  Xs = 0;
  Os = 0;
  
  # iterate over the given board and calculate the amount of Xs and Os on the board
  for y_axis in board:
    for x_axis in y_axis:
      if x_axis == X:
        Xs = Xs + 1;
      elif x_axis == O:
        Os = Os + 1;

  if Xs <= Os:
    return X;
  else:
    return O;
```
Function above will return who is the next player to take move.
```
def actions(board):
  """Returns sets of all possible actions from making move (i,j) on the board."""
  
  possibleActions = set();

  for y, y_axis in enumerate(board):
    for x, x_axis in enumerate(y_axis):
      if x_axis == EMPTY:
        possibleActions.add((y,x))

  return possibleActions;
```
Function above will tell what actions can be took.
```
def results(board, action):
  """Returns the resulted board from making move (i,j) on the board."""
  
  if len(action) != 2:
    raise Exception("Result function: incorrect action");
  if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
    raise Exception("Result function: incorrect function value");
  
  y, x = action[0], action[1];
  boardCopy = copy.deepcopy(board);

  if boardCopy[y][x] != EMPTY:
    raise Exception("Suggested action has already been taken");
  else:
    boardCopy[y][x] = player(board);

  return boardCopy;
```
Function above will return a deep copy of the board that will be used to explore the possibilities available from making a move and then can be used to determine the optimal or suboptimal moves.
```
def winner(board):
  """Returns the winner of the game if there is one."""
  
  # Assume the board is always 3x3
  for y in range(3):
    # Check horizontal lines
    if (board[y][0] == board[y][1] == board[y][2]) and (board[y][0] != EMPTY):
      return board[y][0];
    # Check vertical lines
    if (board[0][y] == board[1][y] == board[2][y]) and (board[0][y] != EMPTY):
      return board[0][y];

  # Check diagonal
  if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
    if (board[1][1] != EMPTY):
      return board[1][1];

  return None;
```
Function above will determine the winner by checking if there is a three Xs or Os in a row horizontally, vertically, or diagonally.
```
def terminal(board):
  """Returns True if the game is over."""
  
  # If there is already a winner, the game is over
  if winner(board) == X or winner(board) == O:
    return True;
  # Check if no empty cells are left
  elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
    return True;
  else:
    return False;
```
Function above will determine whether the game has over.
```
def utility(board):
  """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
  
  if winner(board) == X:
    return 1;
  elif winner(board) == O:
    return -1;
  else:
    return 0;
```
Function above can be used check the if the current game already has a winner or not and can be used to determine the optimal move in minimax.
```
def difficulty(percent=70):
  """Returns True with a certain percentage of possibility, used to make the AI beatable."""
  return random.randrange(100) < percent;
```
Function above will be used to make the computer beatable. The function will be called in the main.py and it will determine whether the computer take the optimal moves using minimax function or suboptimal moves using maximin function.
```
def minimax(board):
  """Returns the optimal action for the current player on the board."""

  if terminal(board):
    return None;

  if player(board) == X:
    score = -math.inf;
    action_to_take = None;

    for action in actions(board):
      min_val = minvalue(results(board, action));

      if min_val > score:
        score = min_val;
        action_to_take = action;

    return action_to_take;

  elif player(board) == O:
    score = math.inf;
    action_to_take = None;
    
    for action in actions(board):
      max_val = maxvalue(results(board, action));
      
      if max_val < score:
        score = max_val;
        action_to_take = action;
        
    return action_to_take;
```
Function above is used to determine the optimal moves for the computer to take.
```
def maximin(board):
  """Returns the unoptimal action for the current player on the board."""

  if terminal(board):
    return None;

  if player(board) == X:
    score = math.inf;
    action_to_take = None;
    
    for action in actions(board):
      max_val = maxvalue(results(board, action));
      
      if max_val < score:
        score = max_val;
        action_to_take = action;
        
    return action_to_take;

  elif player(board) == O:
    score = -math.inf;
    action_to_take = None;

    for action in actions(board):
      min_val = minvalue(results(board, action));

      if min_val > score:
        score = min_val;
        action_to_take = action; 
        
    return action_to_take;
```
Function above is used to determine the suboptimal moves for the computer to take.
```
def minvalue(board):
  """Returns the minimum value out of all maximum values."""

  # If game over, return the utility of state
  if terminal(board):
    return utility(board);
    
  max_value = math.inf; # Iterate over the available actions and return the minimum out of all maximums

  for action in actions(board):
    max_value = min(max_value, maxvalue(results(board, action)));
  
  return max_value;
```
The above function will return the minimum value, used to determine a move that reduces the opponent’s chance of winning.
```
def maxvalue(board):
  """Returns the maximum value out of all minimum values."""

  if terminal(board):
    return utility(board);

  min_value = -math.inf;

  for action in actions(board):
    min_value = max(min_value, minvalue(results(board, action)));

  return min_value;
```
The above function will return the maximum value, used to determine a move that increases the computer’s chance of winning.

# Output and Analysis
The image below is showing what the gameplay looks like. In this case, we will be playing as X which means we go first. For example, we will mark the top-left box with X. After that, the computer will start analysing the next move. Since we have two functions for deciding the computer’s move, the optimal and suboptimal, we know that the computer at some point will choose the suboptimal function instead of the optimal one. After that, the computer takes the move and it marks the top-centre box. After that, we will try to mark the middle-centre box with X, hoping to mark three Xs diagonally. But, after we marked the middle-centre box, the computer marks the middle-right box instead and did not try to block us. From here, we can guess that the computer is using the suboptimal function instead of the optimal one. After that, we mark the bottom-right box with X and we win.

![image](https://user-images.githubusercontent.com/79137636/168089188-adeed76a-6765-4474-9e35-1c318b6b82d9.png)

The image below is showing a different game. We are playing as X, same as before. But the computer this time is using the optimal function rather than suboptimal like the previous one. After we marked the top-left box with X, the computer responded by blocking our way so we can’t make three Xs diagonally. After that, we mark the bottom-left box and the computer responded by blocking us again. This time we can’t make three Xs vertically. Since the O mark has already two in a row horizontally, we will block it from winning by blocking the third box, which happened to be the middle-right box. Then, the game continues until it’s over and we both tie.

![image](https://user-images.githubusercontent.com/79137636/168089268-0eb1a3b1-525a-429f-b5c7-c5aad20f10f5.png)

We can also play as O. However, since X always go first, we will usually wait a little longer because the computer will try to decide the first move. The image below is showing the gameplay when we choose to play as O. First, we will wait for the computer to make the first move. In this case, the computer decided to choose the middle-centre box. We will mark the top-left box so we can make three Os horizontally or vertically. After that, the computer marks the bottom-right box. Then, we mark the middle-left box with O and the computer responded by marking the bottom-left box with X. Since we can no longer make three Os in a row vertically, we will try horizontally by mark the top-right box. After that, the computer mark the bottom-centre box and won the game. In this game we can sure that the function used by the computer to make move is the minimax or the optimal one.

![image](https://user-images.githubusercontent.com/79137636/168089350-99c9baa0-3af8-42f5-b6f5-2fb5dbeaa2c9.png)

Here’s another gameplay. We are playing as O, same as the previous image, but this time it’s tie.

![image](https://user-images.githubusercontent.com/79137636/168089472-fa159178-222b-4501-b731-04a634194552.png)

# Demo
Here's a YouTube link for the demonstration of the program:

https://www.youtube.com/watch?v=bJRGJGH3TeY

# References:
https://medium.com/analytics-vidhya/minimax-algorithm-in-tic-tac-toe-adversarial-search-example-702c7c1030eb 

https://stackoverflow.com/questions/14324472/random-boolean-by-percentage 

https://subakti.com/?page_id=3619 

https://socs.binus.ac.id/2013/04/23/uninformed-search-dan-informed-search/

# Little note
I would like to suggest using replit to run the program. That doesn't mean the program is broken or something. It's just me that I had tried using replit and personally it's very easy for me.
