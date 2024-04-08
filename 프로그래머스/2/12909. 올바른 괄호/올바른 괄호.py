def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []: # 오른쪽 괄호로 시작할경우
                return False
            else:
                stack.pop()
    if stack != []: # 다 끝났는데 왼쪽 괄호가 스택에 남아있을경우
        return False
    return True

