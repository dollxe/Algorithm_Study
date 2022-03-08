from collections import defaultdict

def solution(id_list, report, k):
    answer = {id_: 0 for id_ in id_list}
    progress = defaultdict(set)
    for s in report:
        u1, u2 = s.split(' ')
        progress[u2].add(u1)

    for id_ in id_list:
        if len(progress[id_]) >= k:
            for u in progress[id_]:
                answer[u] += 1
    
    return [answer[i] for i in id_list]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))