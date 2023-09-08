def solution(new_id):
    new_id = new_id.lower() # 1단계
    answer = ''
    allowChar = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    answer += ''.join(i for i in new_id if i in allowChar) # 2단계
    while ".." in answer:
        answer = answer.replace("..", ".") # 3단계
    answer = answer.strip('.') # 4단계
    answer = 'a' if answer == '' else answer # 5단계
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer # 6단계
    answer = answer.ljust(3, answer[-1]) if len(answer) <= 2 else answer # 7단계
    return answer