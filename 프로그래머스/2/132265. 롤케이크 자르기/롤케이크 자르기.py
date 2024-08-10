from collections import Counter

def solution(topping):
    answer = 0
    me = Counter(topping)
    bro = {}

    for i in range(len(topping)) :
        if topping[i] in bro :
            bro[topping[i]] += 1
        else :
            bro[topping[i]] = 1
        me[topping[i]] -= 1

        if me[topping[i]] == 0 :
            del me[topping[i]]

        if len(bro) == len(me) :
            answer +=1

    return answer
