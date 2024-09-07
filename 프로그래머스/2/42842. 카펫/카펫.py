def solution(brown, yellow):
    total = brown + yellow # 12
    for i in range(3, int(total**0.5)+1): # 3~3.6
        if total % i ==0:
            j = total // i
            if (j -2) * (i -2) == yellow:
                return [j, i]
