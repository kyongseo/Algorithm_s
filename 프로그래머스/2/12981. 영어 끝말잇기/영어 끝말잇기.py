def solution(n, words):

    a = [words[0]]
    for i in range(1, len(words)):
        if words[i][0] == words[i-1][-1] and words[i] not in a:
            a.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]

    return [0,0]