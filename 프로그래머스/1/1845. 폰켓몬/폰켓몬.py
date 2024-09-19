def solution(nums):
    choose_len = len(nums) // 2
    temp = list(set(nums))
    temp_len = len(temp)

    if temp_len < choose_len:
        return temp_len
    else:
        return choose_len
            