from itertools import permutations

def solution(numbers):
    r = []
    for i in range(1, len(numbers) + 1):
        for j in permutations(list(numbers), i):
            num = int(''.join(j))
            for k in range(2, num):
                if num % k == 0:
                    break
            else:
                if num not in r and num != 0 and num != 1:
                        r.append(num)
    return len(r)