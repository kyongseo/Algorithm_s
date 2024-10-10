n = int(input())

peoples = list(map(int, input().split()))

peoples.sort()
answer = 0

for i in range(n): 
  answer += sum(peoples[:i+1])

print(answer)