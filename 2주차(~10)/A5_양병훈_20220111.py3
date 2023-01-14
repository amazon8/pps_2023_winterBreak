def solution(skill, skill_trees):
    '''
    시작: 11:41
    1. for --> 스킬 순서 맞는지 체크
    '''
    
    answer = -1
    fail = 0
    
    for i in range(len(skill_trees)):
        temp = list(skill)
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in temp:
                if skill_trees[i][j] != temp[0]:
                    fail += 1
                    break
                else:
                    del temp[0]
    
    return len(skill_trees)-fail