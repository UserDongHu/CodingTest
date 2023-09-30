def solution(age):
    table = str.maketrans('0123456789', 'abcdefghij')
    return str(age).translate(table)