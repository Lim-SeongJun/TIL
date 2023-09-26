def solution(n):
    answer = 0
    for i in range(n+1,1000000):
        if bin(i)[2:].count('1') == bin(n).count('1'):
            answer += i
            break
    return answer