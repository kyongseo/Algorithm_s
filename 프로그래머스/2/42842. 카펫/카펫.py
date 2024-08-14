def solution(brown, yellow):
    total = brown + yellow
    for weight in range(total, 2, -1):
        if total % weight == 0: 
            height = total // weight 
            
            if yellow == (weight-2) * (height-2):
                return [weight, height]