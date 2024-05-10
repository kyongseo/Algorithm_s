from queue import deque
from collections import defaultdict

directions = (0, 1, 0, -1, 0)

def bfs(i, j, n, m, oil, land):
    amount = 1
    land[i][j] = oil
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx, ny = x + directions[d], y + directions[d+1]
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                amount += 1
                land[nx][ny] = oil
                que.append((nx, ny))
                
    return amount

def solution(land):
    answer, oil = 0, 2
    n, m = len(land), len(land[0])
    amount_of = defaultdict(int)

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                amount_of[oil] = bfs(i, j, n, m, oil, land)
                oil += 1
                
    for j in range(m):
        oil_types = set([land[i][j] for i in range(n)])
        amount = 0
        for oil in oil_types:
            amount += amount_of[oil]
        answer = max(amount, answer)
    
    return answer