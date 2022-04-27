import sys
input = sys.stdin.readline

history_of_move = []

def hanoi(n, s_point, e_point):
  if n == 1:
    history_of_move.append((s_point, e_point))
    return

  b_point = 6 - (s_point+e_point)
  hanoi(n-1, s_point, b_point)
  history_of_move.append((s_point, e_point))
  hanoi(n-1, b_point, e_point)

n = int(input())
hanoi(n, 1, 3)
print(len(history_of_move))
for move in history_of_move:
  s, e = move
  print(s, e)
