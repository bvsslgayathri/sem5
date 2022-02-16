squares = [' ']*9
players = 'XO'
board = '''

   {0} | {1} | {2}
 --------------
    {3}| {4} | {5}
 --------------
   {6} | {7} | {8}

  '''
win_conditions = [
                  (0,1,2), (3,4,5), (6,7,8), #horizontals
                  (0,3,6), (1,4,7), (2,5,8), #verticals
                  (0,4,8), (2,4,6)           #diagonals
]

def check_win(player):
  for a,b,c in win_conditions :
    if {squares[a], squares[b], squares[c]} == {player} :
      return True

while True:
  print(board.format(*squares))
  if check_win(players[1]):
    print(players[1],' is the winner !')
    break
  if ' ' not in squares:
    print('It's a tie !')
    break
  move = input(players[1],'to move [0-8] > ')
  if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ' :
    print('Invalid move !')
    continue
  squares[int(move)], players = players[0], players[::-1]
