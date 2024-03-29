def solution(n, lost, reserve):

    reserve_set = set(reserve)
    lost_set = set(lost)
    
    reserve_student = reserve_set - lost_set

    lost_student = lost_set - reserve_set

    for student in reserve_student:
        if (student - 1) in lost_student:
            lost_student.remove(student - 1)
        elif (student + 1) in lost_student:
            lost_student.remove(student + 1)

    return n - len(lost_student)