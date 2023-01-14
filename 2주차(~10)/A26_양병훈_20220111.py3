def solution(x):
    answer = True
    
    x = str(x)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    
    if int(x)%sum==0:
        return True
    else: 
        return False