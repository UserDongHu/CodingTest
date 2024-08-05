def solution(myStr):
    myStr = myStr.replace("abc", "A").replace("acb", "A").replace("bac", "A").replace("bca", "A").replace("cab", "A").replace("cba", "A").replace("ab", "A").replace("ac", "A").replace("ba", "A").replace("bc", "A").replace("ca", "A").replace("cb", "A").replace("a", "A").replace("b", "A").replace("c", "A")
    answer = list(filter(lambda x: x, myStr.split("A")))
    if answer != []:
        return answer
    else:
        return ["EMPTY"]