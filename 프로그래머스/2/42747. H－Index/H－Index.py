def solution(citations):
    
    citations.sort(reverse=True)
    
    for idx, citation in enumerate(citations):
        if citation <= idx:
            return idx
    return len(citations)