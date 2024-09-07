N = int(input())

for _ in range(N): # 0,1,2,3,4
  answer = 0
  sumScore = 0
  quiz = input()
  for i in quiz:
    if i == "O":
      answer += 1
    else:
      answer = 0
    sumScore += answer
  print(sumScore)