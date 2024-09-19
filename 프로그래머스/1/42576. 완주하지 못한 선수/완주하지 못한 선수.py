from collections import deque

def solution(participant, completion):
    # 리스트를 deque로 변환
    participant = deque(sorted(participant))
    completion = deque(sorted(completion))

    while completion:
        p_name = participant.popleft()
        c_name = completion.popleft()

        if p_name != c_name:
            return p_name

    return participant[0]
      