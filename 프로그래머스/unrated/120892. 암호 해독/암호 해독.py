def solution(cipher, code):
    answer = ''
    myindex = code - 1
    while True:
        if myindex >= len(cipher):
            break
        answer += cipher[myindex]
        myindex += code
    return answer