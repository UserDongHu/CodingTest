from itertools import product

def solution(word):
    mydic = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            myword = ""
            for k in j:
                myword += k
            mydic.append(myword)
    mydic.sort()
    for i, j in enumerate(mydic):
        if j == word:
            return i+1