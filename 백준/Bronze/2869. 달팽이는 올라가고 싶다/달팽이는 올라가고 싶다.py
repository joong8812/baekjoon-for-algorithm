a, b, v = map(int, input().split())

move_a_day = a - b
left_v_before_last_climb = v - a
if left_v_before_last_climb % move_a_day > 0:
  print(left_v_before_last_climb // move_a_day + 2)
else:
  print(left_v_before_last_climb // move_a_day + 1)