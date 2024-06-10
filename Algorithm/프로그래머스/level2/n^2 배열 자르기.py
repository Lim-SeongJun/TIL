def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer += [max(i//n,i%n)+1]
    return answer