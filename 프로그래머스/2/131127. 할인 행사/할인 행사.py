def solution(want, number, discount):

    answer = 0 
    s = []
    for i in range(len(want)):
        for j in range(number[i]):
            s.append(want[i])
    s.sort()
    for i in range(len(discount) - 9):
        list_10 = discount[i:i+10]
        list_10.sort()

        if list_10 == s:
            answer += 1
    return answer