def solution(elements):
    le = []
    elements = elements + elements
    for i in range(1, len(elements) // 2 + 1):
        for j in range(len(elements) // 2):
            n = sum(elements[j:i+j])
            le.append(n)

    return len(set(le))