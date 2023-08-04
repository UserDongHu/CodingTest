def isTrue(n):
        a = []
        for i in n:
            if len(a) == 0:
                a.append(i)
            else:
                if i == ')' and a[-1] == '(':
                    a.pop()
                elif i == ']' and a[-1] == '[':
                    a.pop()
                elif i == '}' and a[-1] == '{':
                    a.pop()
                else:
                    a.append(i)
        if len(a) == 0:
            return True
        else:
            return False
def solution(s):
    answer = 0
    a = list(s)
    if isTrue(a):
        answer += 1
    for i in range(len(a)-1):
        temp = a[0]
        for j in range(len(a)-1):
            a[j] = a[j+1]
        a[-1] = temp
        if isTrue(a):
            answer += 1
    return answer