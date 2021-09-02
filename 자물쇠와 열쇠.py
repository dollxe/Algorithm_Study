import copy, pprint

def rotate(key):
    return list(map(list, zip(*(key[::-1]))))

def check(x, y, key, metrix):
    padding = len(key) - 1
    new_metrix = copy.deepcopy(metrix)

    for i, row in enumerate(key):
        for j, value in enumerate(row):
            if value == 0: continue
            if metrix[i+x][j+y] == 1: return False
            new_metrix[i+x][j+y] = value
    
    # pprint.pprint(new_metrix)

    for row in new_metrix[padding:-padding]:
        for value in row[padding:-padding]:
            if value == 0: return False
    
    return True
            
def solution(key, lock):
    padding = len(key) - 1
    metrix = [[0 for i in range(len(lock)+(padding*2))] for j in range(len(lock)+(padding*2))]

    for i, row in enumerate(lock):
        for j, value in enumerate(row):
            metrix[i+padding][j+padding] = value

    for x in range(len(metrix)-padding):
        for y in range(len(metrix)-padding):
            for _ in range(4):
                if check(x, y, key, metrix):
                    return True
                key = rotate(key)

    # print(check(x, y, key, metrix))

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))