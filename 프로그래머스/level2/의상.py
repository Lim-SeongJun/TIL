def solution(clothes):
    answer = 1
    dic = dict()
    for i in clothes:
        if dic.get(i[1]) == None:
            dic[i[1]] = [i[0]]
        else:
            dic[i[1]].append(i[0])
    for i in dic.values():
        answer *= len(i)+1
    return answer - 1