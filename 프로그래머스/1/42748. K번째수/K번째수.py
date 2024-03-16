
def solution(array, commands):
    return list(map(lambda commands : sorted(array[commands[0]-1:commands[1]])[commands[2]-1], commands))

