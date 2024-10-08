from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while len(people) > 1 :
        back = people.pop()
        if back + people[0] <= limit:
            answer += 1
            people.popleft()
        else:
            answer += 1
    if len(people) == 1 and people[0] <= limit:
        answer += 1

    return answer