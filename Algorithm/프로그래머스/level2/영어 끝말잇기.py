def solution(n, words):
    check = [words[0]]
    for i in words[1:]:
        if (i in check) or check[-1][-1]!=i[0]:
            print(check, n,i[0])
            return [len(check)%n+1 ,(len(check)//n)+1]
        check.append(i)
    return [0,0]