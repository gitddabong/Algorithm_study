# import sys

# input = sys.stdin.readline
read_f = open("/Users/jeong-wonjong/Desktop/jungle/Algorithm_study/baekjoon challenge 100/inp.txt", 'r')
write_f = open("/Users/jeong-wonjong/Desktop/jungle/Algorithm_study/baekjoon challenge 100/out.txt", 'w')
input = read_f.readline

n, m = map(int, input().split())

weights = list(map(int, input().split()))

weights.sort(reverse=True)
cnt = 0
while weights:
  target = weights.pop(0)
  for i, weight in enumerate(weights):
    if target + weight <= m:
      weights.pop(i)
      break
  
  cnt += 1

write_f.write(str(cnt))

read_f.close()
write_f.close()