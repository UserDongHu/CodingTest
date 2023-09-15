def solution(want, number, discount):
    answer = 0
    product = []
    for i, j in zip(want, number):
        product += [i]*j
    product.sort()
    
    for i in range(len(discount) - 9):
            if product == sorted(discount[i:i+10]):
                answer += 1
    return answer