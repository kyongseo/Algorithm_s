from collections import deque
import sys

deq = deque()
n = int(input())

for _ in range(n):
  s = sys.stdin.readline().split()
  
  if s[0] == "push":
    deq.append(int(s[1]))
    
  elif s[0] == "pop":
    if len(deq) > 0:
      print(deq.popleft())
    else:
      print(-1)
      
  elif s[0] == "front":
    if len(deq) > 0:
      print(deq[0])
    else:
      print(-1)
      
  elif s[0] == "back":
    if len(deq) > 0:
      print(deq[-1])
    else:
      print(-1)
      
  elif s[0] == "size":
    print(len(deq))

  elif s[0] == "empty":
    if len(deq) > 0:
      print(0)
    else:
      print(1)
