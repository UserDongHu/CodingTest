from collections import deque

def solution(order):
    answer = 0
    mybox = deque(i+1 for i in range(len(order)))
    mybelt = deque()
    order = deque(order)

    while order:
        if mybox and mybox[0] == order[0]:
            mybox.popleft()
            order.popleft()
            answer += 1
        elif mybelt and mybelt[-1] == order[0]:
            mybelt.pop()
            order.popleft()
            answer += 1
        else:
            if mybox:
                mybelt.append(mybox.popleft())
            else:
                break

    return answer
