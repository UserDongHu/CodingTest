def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        myskill = ""
        for j in i:
            if j in skill:
                myskill += j
        if myskill == skill[:len(myskill)]:
            answer += 1
    return answer