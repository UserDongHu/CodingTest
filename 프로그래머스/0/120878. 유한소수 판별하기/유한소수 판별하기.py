import fractions
def solution(a, b):
    myf = fractions.Fraction(a, b)
    a = myf.numerator
    b = myf.denominator
    myarray = [i for i in range(2, b+1) if b%i == 0]
    if all(i%2 == 0 or i%5 == 0 for i in myarray):
        return 1
    return 2