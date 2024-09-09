from collections import Counter

def solution(a, b, c, d):
    myCounter = Counter([a, b, c, d]).most_common()
    
    if myCounter[0][1] == 4:
        return 1111*a
    elif myCounter[0][1] == 3:
        return (10 * myCounter[0][0] + myCounter[1][0])**2
    elif myCounter[0][1] == 2 and myCounter[1][1] == 2:
        return (myCounter[0][0] + myCounter[1][0]) * abs(myCounter[0][0] - myCounter[1][0])
    elif myCounter[0][1] == 1:
        return min([a, b, c, d])
    else:
        return myCounter[1][0] * myCounter[2][0]