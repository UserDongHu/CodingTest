import math
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    answer = 1 # 한칸씩 가는거
    a = n // 2 # 최대 두칸의 개수
    b = n % 2 # 최소 한칸의 개수
    if b == 0:
        answer += 1 # 짝수이면 두칸씩만 가는거 추가
        for i in range(1, a):
            answer += math.factorial(a+i) // (math.factorial(i*2) * math.factorial(a-i))
    else:
        answer += a+b # 1한개일때 추가
        for j in range(1, a):
            answer += math.factorial(a+b+j) // (math.factorial(j*2+b) * math.factorial(a-j))
    return answer % 1234567