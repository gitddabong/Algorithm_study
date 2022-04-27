n = int(input())

cnt = 0
for hour in range(n + 1):
  for minute in range(60):
    for second in range(60):
      temp = str(hour) + str(minute) + str(second)
      if '3' in temp:
        cnt += 1

print(cnt)