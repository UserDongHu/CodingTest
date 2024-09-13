def solution(lottos, win_nums):
    win_count = 0
    zero_count = 0
    for i in lottos:
        if i in win_nums:
            win_count += 1
        elif i == 0:
            zero_count += 1
    answer = [7-win_count-zero_count, 7-win_count]
    for i in range(2):
        if answer[i] == 7:
            answer[i] = 6
    return answer