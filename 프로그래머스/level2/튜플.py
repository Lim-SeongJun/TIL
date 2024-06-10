def solution(s):
    dic = {}
    s = s.replace('{','')
    s = s.replace('}','')
    s = list(map(int,s.split(',')))
    for i in set(s):
        dic[i]=s.count(i)
    a = list(dic.items())
    a.sort(key=lambda x : -x[1])
    b,c = list(zip(*a))
    return list(b)