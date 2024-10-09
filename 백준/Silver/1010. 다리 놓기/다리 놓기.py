from math import comb

def combina(n,m):
  return comb(m, n)

n = int(input())

for _ in range(n):
  n , m = map(int, input().split())
  print(combina(n, m))