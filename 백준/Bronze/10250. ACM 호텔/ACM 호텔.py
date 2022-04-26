import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  floor = h if n%h == 0 else n%h
  room_no = n//h if n%h == 0 else n//h+1
  room_no = f"0{room_no}" if room_no < 10 else room_no
  print(f"{floor}{room_no}")