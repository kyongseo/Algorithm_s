import sys

n = int(sys.stdin.readline().strip())
exit_cards = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())
find_cards = list(map(int, sys.stdin.readline().strip().split()))

dic = {}

for i in exit_cards:
  if i in dic:
    dic[i] += 1

  else:
    dic[i] = 1

for j in find_cards:
  if j in dic:
    print(dic[j], end=' ')
  else:
    print(0, end=' ')