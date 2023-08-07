def solution(n, lost, reserve):
    
    reserve = list(reserve)
    can = 0

    for i in lost:
        if(len(reserve) > 0):
            if(i+1 in reserve):
                a = reserve.remove(i+1)
                can += 1

            elif(i-1 in reserve):
                b = reserve.remove(i-1)
                can += 1
        
    answer = n - len(lost) + can
    return answer

print(solution(5, [1,2,3], [2,3,4]))