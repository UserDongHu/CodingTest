def solution(quiz):
    answer = []
    for i in quiz:
        myarray = i.split()
        if myarray[1] == '+':
            answer.append("O") if int(myarray[0]) + int(myarray[2]) == int(myarray[4]) else answer.append("X")
        else:
            answer.append("O") if int(myarray[0]) - int(myarray[2]) == int(myarray[4]) else answer.append("X")
    return answer