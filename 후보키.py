import collections
from itertools import combinations, permutations

def rtn_all_combinations(li):
    combs = [e for e in li]
    for i in range(2, len(li)+1):
        for comb in combinations(li, i):
            combs.append(tuple(comb))
    return combs


def solution(relation):
    answer = set()
    row_num = len(relation)
    col_num = len(relation[0])
    col_list = range(col_num)
    candidate_keys = rtn_all_combinations(col_list)

    for candidate_key in candidate_keys:
        temp_list = []
        
        for t in relation:
            tuple_info = []
            
            try:
                for key in candidate_key:
                    tuple_info.append(t[key])
                temp_list.append(tuple(tuple_info))
            except:
                temp_list.append(t[candidate_key])
        
        if len(set(temp_list)) == row_num:
            print('check')
            try:
                for c in rtn_all_combinations(candidate_key):
                    print(c, candidate_key)
                    if c != candidate_key and c in answer:
                        break
                else:
                    answer.add(candidate_key)
            except:
                answer.add(candidate_key)

    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
