def solution(my_string):
    myarray = my_string.split(' ')
    sum = int(myarray[0])
    for i in range(1, len(myarray), 2):
        if myarray[i] == '-':
            sum -= int(myarray[i + 1])
        else:
            sum += int(myarray[i + 1])
    return sum