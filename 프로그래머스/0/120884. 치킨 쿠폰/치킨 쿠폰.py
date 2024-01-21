def solution(chicken):
    coupon = 0
    answer = 0
    while chicken:
        chicken -= 1
        coupon += 1
        if coupon >= 10:
            answer += 1
            coupon -= 9
    return answer