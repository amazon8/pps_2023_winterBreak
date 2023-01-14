def solution(s):
    
    s = s.upper()
    
    pNum = s.count("P")
    yNum = s.count("Y")
    
    if pNum != yNum:
        return False
    
    return True