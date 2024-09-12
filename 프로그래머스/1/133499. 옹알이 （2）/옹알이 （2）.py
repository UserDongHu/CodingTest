import re

def solution(babbling):
    answer = 0
    possible_sounds = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # 연속된 같은 발음이 있으면 무시
        if re.search(r'(aya|ye|woo|ma)\1', word):
            continue
        
        # 발음들이 단순 반복된 패턴인지 확인
        temp = word
        for sound in possible_sounds:
            temp = temp.replace(sound, ' ')
        
        # 발음 가능한 경우만 카운트
        if temp.strip() == '':
            answer += 1
    
    return answer