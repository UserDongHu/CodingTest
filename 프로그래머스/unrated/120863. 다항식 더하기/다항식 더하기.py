def solution(polynomial):
    myx, mynum = 0, 0
    mypoly = polynomial.split()

    for term in mypoly:
        if term == '+':
            continue
        if 'x' in term:
            if term == 'x':
                myx += 1
            else:
                myx += int(term[:-1])
        else:
            mynum += int(term)

    x = '' if myx == 0 else 'x' if myx == 1 else f'{myx}x'
    num = '' if mynum == 0 else str(mynum)

    return x if not num else num if not x else f'{x} + {num}'