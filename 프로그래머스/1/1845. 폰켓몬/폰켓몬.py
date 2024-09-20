def solution(nums):
    choose_len = len(nums) // 2
    temp_len = len(list(set(nums)))

    if choose_len < temp_len:
        return choose_len
    else:
        return temp_len
            