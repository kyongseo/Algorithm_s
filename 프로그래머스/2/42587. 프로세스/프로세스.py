from collections import deque

def solution(prioriries, location):
    answer = 0
    deq = deque([v, i] for i,v in enumerate(prioriries))
    while deq:
        item = deq.popleft()
        if deq and max(deq)[0] > item[0]:
            deq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
