import colorama
import os

os.system('color')

player = 0
board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

playerWon = -1
while playerWon == -1:
  print(f'player {player + 1} to play')

  icons = [f' ', f'{colorama.Fore.RED}X{colorama.Style.RESET_ALL}', f'{colorama.Fore.GREEN}O{colorama.Style.RESET_ALL}']

  print(f' 1 2 3')
  print(f'1{icons[board[0][0] + 1]}│{icons[board[0][1] + 1]}│{icons[board[0][2] + 1]}')
  print(f' ─┼─┼─')
  print(f'2{icons[board[1][0] + 1]}│{icons[board[1][1] + 1]}│{icons[board[1][2] + 1]}')
  print(f' ─┼─┼─')
  print(f'3{icons[board[2][0] + 1]}│{icons[board[2][1] + 1]}│{icons[board[2][2] + 1]}')

  move = input('select a space: ')
  x = int(move[0]) - 1
  y = int(move[2]) - 1

  while x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != -1:
    move = input('select a valid space: ')
    x = int(move[0]) - 1
    y = int(move[2]) - 1

  board[x][y] = player

  player = (player + 1) % 2

  if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != -1:
    playerWon = board[0][0]
  if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != -1:
    playerWon = board[1][0]
  if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != -1:
    playerWon = board[2][0]
  if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != -1:
    playerWon = board[0][0]
  if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != -1:
    playerWon = board[0][1]
  if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != -1:
    playerWon = board[0][2]
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != -1:
    playerWon = board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != -1:
    playerWon = board[2][0]

print(f'player {playerWon + 1} has won')
print(f'')
print(f'{icons[board[0][0] + 1]}│{icons[board[0][1] + 1]}│{icons[board[0][2] + 1]}')
print(f'─┼─┼─')
print(f'{icons[board[1][0] + 1]}│{icons[board[1][1] + 1]}│{icons[board[1][2] + 1]}')
print(f'─┼─┼─')
print(f'{icons[board[2][0] + 1]}│{icons[board[2][1] + 1]}│{icons[board[2][2] + 1]}')
