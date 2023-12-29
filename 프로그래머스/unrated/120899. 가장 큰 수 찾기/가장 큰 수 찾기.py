def solution(array):
    answer = [max_array := max(array)]
    answer.extend([i for i in range(len(array)) if array[i] == max_array])
    return answer