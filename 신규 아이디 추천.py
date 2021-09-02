import re

def solution(new_id:str):

    answer = new_id.lower()
    
    # r = re.compile('[^-_.a-z0-9]')
    answer = re.sub('[^-_.a-z0-9]', '', answer)

    answer = re.sub('[.]+', '.', answer)
    
    answer = answer.strip('.')

    if not answer: answer += 'a'

    if len(answer) >= 16: answer = answer[:15].strip('.')
    
    while len(answer) <= 2:
        answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))