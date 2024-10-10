n, k = map(int, input().split())

answer = 0
coins = []

for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
  if k >= coin:
    answer += k // coin
    k %= coin
    if k<=0:
      break

print(answer)