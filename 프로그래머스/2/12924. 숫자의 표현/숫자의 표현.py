def solution(n):     
    count = 0

    for i in range(1, n+1):
        answer = 0
        for j in range(i, n+1):
            answer += j
            if answer == n:
                count += 1
                break
            if answer > n:
                break
    return count
