def solution(elements):
    extended_elements = elements + elements
    unique_sums = set()  

    n = len(elements)  

    for length in range(1, n + 1):
        for start in range(n):
            part_sum = sum(extended_elements[start:start + length])
            unique_sums.add(part_sum)
            
    return len(unique_sums)