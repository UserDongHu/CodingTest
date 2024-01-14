def solution(spell, dic):
    myspell = ''.join(sorted(spell))
    print(myspell)
    for i in dic:
        if myspell == ''.join(sorted([j for j in i])):
            return 1
    return 2