def solution(s): 
    if ((len(s) == 4) | (len(s)==6)) & s.isdecimal(): 
        return True 
    else: 
        return False