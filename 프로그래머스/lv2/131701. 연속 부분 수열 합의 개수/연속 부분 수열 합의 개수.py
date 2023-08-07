def solution(elements):
    sum = elements[:]
    for i in range(1, len(elements)+1):
        if i > 1:
            for j in range(len(elements)):
                index = (j+i-1)%len(elements)
                sum.append(sum[(i-2)*len(elements)+j] + sum[index])
    return len(list(set(sum)))