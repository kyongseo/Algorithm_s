def solution(food):
    answer = ''
    for i in range(1, len(food)): # 1,2,3
        answer += str(i) * (food[i]//2)
    return answer + '0' + answer[::-1]