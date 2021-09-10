from collections import deque, defaultdict
import heapq

def make_graph(li, n):
    g = {node:[] for node in range(1, n+1)}
    
    for s, e, distance in li:
        g[s].append((e, distance))
        g[e].append((s, distance))
    
    return g

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0    ## 시작값 0
    q = []
    heapq.heappush(q, (start, distances[start]))

    while q:
        now_pos, now_distance = heapq.heappop(q)

        if now_distance > distances[now_pos]: continue
        # 기존의 거리보다 길면 continue

        for next_pos, next_distance in graph[now_pos]:
            candidate_distance = now_distance + next_distance
            if candidate_distance < distances[next_pos]:
                distances[next_pos] = candidate_distance
                heapq.heappush(q, (next_pos, candidate_distance))
    
    return distances
    

def solution(n, s, a, b, fares):
    answer = float('inf')

    g = make_graph(fares, n)

    dp = [[]] + [dijkstra(g, i) for i in range(1, n+1)]

    for i in range(1, n+1):  # 합승 목적지
        if i != s:
            distance = dp[i][s]
        else:
            distance = 0
        distance += dp[i][a] + dp[i][b]
        if distance < answer:
            answer = distance

    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))