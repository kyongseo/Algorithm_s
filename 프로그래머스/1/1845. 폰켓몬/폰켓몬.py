def solution(nums):
    answer = 0
    chosen_length=len(nums)//2
    tmp=set(nums)
    num_li=list(tmp)
    answer_leng=len(num_li)
    
    if chosen_length<answer_leng:
        answer=chosen_length
    else:
        answer=answer_leng
        
    return answer
            