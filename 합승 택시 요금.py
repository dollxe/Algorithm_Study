from collections import deque, defaultdict

def make_graph(li):
    g = defaultdict(list)
    
    for s, e, distance in li:
        g[s].append((e, distance))
        g[e].append((s, distance))
    
    return g

def bfs(start, end, graph):
    q = deque([(start, 0)])
    total_distance = 0

    while q:
        now_pos, now_distance = q.popleft()
        total_distance += now_distance

        if now_pos == end: break

        for pos, distance in graph[now_pos]:
            q.append((pos, distance))
     
    return total_distance

def solution(n, s, a, b, fares):
    answer = 0

    g = make_graph(fares)

    _1 = bfs(s, a, g) + bfs(a, b, g)
    _2 = bfs(s, b, g) + bfs(b, a, g)

    if _1 > _2:
        answer = _2
    else:
        answer = _1

    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))