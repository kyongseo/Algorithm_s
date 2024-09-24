def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict:
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1

    for key in dict.keys():
        answer *= (dict[key] + 1)

    return answer -1