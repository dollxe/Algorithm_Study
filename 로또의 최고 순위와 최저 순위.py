def solution(lottos, win_nums):
    grade = {i:7-i for i in range(7)}
    grade[0] = 6
    win_nums = set(win_nums)
    match = 0
    _0_cnt = 0

    for num in lottos:
        if num in win_nums: match += 1
        elif num == 0: _0_cnt += 1

    # if  match == 0 and _0_cnt == 0: return [6,6]
    top_match = min(6, 7 - (match + _0_cnt))
    bottom_match = min(6, 7 - match)
    return [top_match, bottom_match]

if __name__ == '__main__':
    print(solution([18, 19, 13, 3, 17, 45], [31, 2, 44, 1, 6, 25]))