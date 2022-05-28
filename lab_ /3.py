def solution(n, m, x_axis, y_axis):
  answer = 0

  x_nums = x_axis + [n]
  y_nums = y_axis + [m]

  x_left = 0
  for x_right in x_nums:
    width = x_right - x_left

    y_left = 0
    for y_right in y_nums:
      height = y_right - y_left
      answer = max(answer, width * height)
      y_left = y_right
    
    x_left = x_right

  return answer

print(solution(4, 4, [1], [3])) # answer = 9
print(solution(3, 4, [1], [1,2])) # answer = 4