def solution(keymap, targets):
    answer = []
    myresult = 0
    for i in targets:
        for j in i:
            myfilterlist = list(filter(lambda x: x != 0, [k.find(j)+1 for k in keymap]))
            if len(myfilterlist) == 0:
                myresult = -1
                break
            else:
                myresult += min(myfilterlist)
        answer.append(myresult)
        myresult = 0
        
    return answer