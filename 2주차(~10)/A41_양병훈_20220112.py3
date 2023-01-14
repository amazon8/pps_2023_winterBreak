def solution(s):
    '''
    시작: 11:54
    1. " " or i=0 --> 대문자로 
    '''
    s = s.lower()
    s = list(s)
    for i in range(len(s)):
        if i==0:
            s[i] = s[i].upper()
        if i != len(s)-1 and s[i] == " ":
            s[i+1] = s[i+1].upper()
    
    s = "".join(s)
    return s