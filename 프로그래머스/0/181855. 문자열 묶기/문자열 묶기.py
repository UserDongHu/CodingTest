def solution(strArr):
    mydict = {}
    for i in strArr:
        if len(i) in mydict:
            mydict[len(i)] += 1
        else:
            mydict[len(i)] = 1
    return max(mydict.values())