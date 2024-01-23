def solution(before, after):
    for i in after:
        before = before.replace(i, '', 1)
    return 1 if before == '' else 0