import math
import copy
import random

X = "X";
O = "O";
EMPTY = None;

def initialState():
  """Returns the starting state of the board where all the 9 slots from the 3x3 board is empty."""
  
  return [[EMPTY, EMPTY, EMPTY], 
          [EMPTY, EMPTY, EMPTY], 
          [EMPTY, EMPTY, EMPTY]]


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


def actions(board):
  """Returns sets of all possible actions from making move (i,j) on the board."""
  
  possibleActions = set();

  for y, y_axis in enumerate(board):
    for x, x_axis in enumerate(y_axis):
      if x_axis == EMPTY:
        possibleActions.add((y,x))

  return possibleActions;


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


def utility(board):
  """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
  
  if winner(board) == X:
    return 1;
  elif winner(board) == O:
    return -1;
  else:
    return 0;


def difficulty(percent=55):
  """Returns True with a certain percentage of possibility, used to make the AI beatable."""
  return random.randrange(100) < percent;

  
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


def minvalue(board):
  """Returns the minimum value out of all maximum values."""

  # If game over, return the utility of state
  if terminal(board):
    return utility(board);
    
  max_value = math.inf; # Iterate over the available actions and return the minimum out of all maximums

  for action in actions(board):
    max_value = min(max_value, maxvalue(results(board, action)));
  
  return max_value;

def maxvalue(board):
  """Returns the maximum value out of all minimum values."""

  if terminal(board):
    return utility(board);

  min_value = -math.inf;

  for action in actions(board):
    min_value = max(min_value, minvalue(results(board, action)));

  return min_value;
