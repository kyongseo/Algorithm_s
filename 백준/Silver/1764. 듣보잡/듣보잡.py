n, m = map(int, input().split())

a = set()
b = set()

for _ in range(n):
  a.add(input())

for _ in range(m):
  b.add(input())

answer = sorted(list(a & b))

print(len(answer))

for i in answer:
  print(i)