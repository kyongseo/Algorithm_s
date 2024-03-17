def solution(x):
    num = 0
    for i in list(str(x)):
        num += int(i) #1
    if x % num == 0: # 10 % 1 == 0 나머지
        answer = True 
    else:
        answer = False
    return answer

# return x % sum([int(c) for c in str(x)]) == 0
