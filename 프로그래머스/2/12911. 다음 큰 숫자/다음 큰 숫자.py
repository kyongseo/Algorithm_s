def solution(n):
    c = bin(n).count("1")
    for i in range(n+1,1000001):
        if bin(i).count("1") == c:
            return i