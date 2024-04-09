from collections import deque
def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            while progresses:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
            answer.append(cnt)
    return answer