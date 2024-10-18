from collections import deque
import sys

n = int(input())
cards = deque()

for _ in range(n):
  com = sys.stdin.readline().split()
  
  if com[0] == "push_back":
    cards.append(com[1])
  elif com[0] == "push_front":
    cards.appendleft(com[1])
  elif com[0] == "pop_front":
    if len(cards) > 0:
      print(cards[0])
      cards.popleft()
    else:
      print(-1)
  elif com[0] == "pop_back":
    if len(cards) > 0:
      print(cards[-1])
      cards.pop()
    else:
      print(-1)
  elif com[0] == "size":
    print(len(cards))
  elif com[0] == "empty":
    if len(cards) == 0:
      print(1)
    else:
      print(0)
  elif com[0] == "front":
    if len(cards) == 0:
      print(-1)
    else:
      print(cards[0])
  elif com[0] == "back":
    if len(cards) == 0:
      print(-1)
    else:
      print(cards[-1])