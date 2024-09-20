from collections import deque

def solution(participant, completion):

    participant.sort()
    completion.sort()

    participant = deque(participant)
    completion = deque(completion)
    
    while completion:
        p_name = participant.popleft()
        c_name = completion.popleft()

        if p_name != c_name:
            return p_name

    return participant[0]