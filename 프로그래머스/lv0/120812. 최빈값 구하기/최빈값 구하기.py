import collections
def solution(array):
    myarray = collections.Counter(array).most_common()
    try:
        return -1 if myarray[0][1] == myarray[1][1] else myarray[0][0]
    except:
        return myarray[0][0]