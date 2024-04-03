def solution(maps):
    w = len(maps) - 1
    h = len(maps[0]) - 1
    visit = set() 
    going = [[0,0,1]]
    while going:
        now = going.pop(0)
        x, y, count = now[0], now[1], now[2]
        if x == w and y == h:
            return count
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= w and 0 <= ny <= h and (nx, ny) not in visit and maps[nx][ny] == 1:
                going.append([nx, ny, count + 1])
                visit.add((nx,ny))
    return -1