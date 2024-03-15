def solution(x, n):
   # return  [x*i for i in range(1, n+1)]
    list = []
    for i in range(1, n+1):
        list.append(x*i)
    return list