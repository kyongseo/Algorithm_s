n = int(input())

for _ in range(n):
  s = input()
  arr = []
  
  for i in s:
    if i == '(':
      arr.append('(')
    elif i == ')':
      if len(arr) == 0:
        arr.append(')')
        break
      else:
        arr.pop()

  if len(arr) != 0:
    print('NO')
  else:
    print('YES')