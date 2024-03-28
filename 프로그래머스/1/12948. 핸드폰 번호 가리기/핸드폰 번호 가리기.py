def solution(phone_number):
    num = len(phone_number)
    back = phone_number[-4:]
    return "*"*(num-4) + back