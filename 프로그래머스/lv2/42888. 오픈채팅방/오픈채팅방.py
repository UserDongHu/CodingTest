def solution(record):
    userinfo = {}
    answer = []
    for text in record:
        info = text.split(' ')
        if info[0] == 'Enter':
            userinfo[info[1]] = info[2]
            answer.append(info[1]+'님이 들어왔습니다.')
        elif info[0] == 'Leave':
            answer.append(info[1]+'님이 나갔습니다.')
        elif info[0] == 'Change':
            userinfo[info[1]] = info[2]
    answer = list(map(lambda x: x.replace(x.split('님')[0], userinfo[x.split('님')[0]]), answer))
    
    return answer