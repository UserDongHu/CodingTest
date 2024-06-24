def solution(myString, pat):
    return 1 if pat.replace("A", "b").replace("B", "A").replace("b", "B") in myString else 0