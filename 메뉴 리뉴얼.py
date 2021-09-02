from collections import defaultdict, Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        sets = defaultdict(int)
        for order in orders:
            for c in list(combinations(order, i)):
                sets[(''.join(sorted(c)))] += 1

        # 다른 사람의 Counter를 사용한 코드. 참고용.
        # order_combinations = []
        # for order in orders:
        #     order_combinations += combinations(sorted(order), i)
        # most_ordered = Counter(order_combinations).most_common()
        # answer += [''.join(s) for s, cnt in most_ordered if cnt == max(sets.values()) and cnt >= 2]
        
        answer += [s for s, cnt in sets.items() if cnt == max(sets.values()) and cnt >= 2]

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))