N = int(input())

A = set(map(int, input().split()))
M = int(input())
exit = list(map(int, input().split()))
for i in exit:
  if i in A:
      print(1)
  else:
      print(0)