def solution(want, number, discount):
    answer = 0
    length = len(discount) - 9
    for i in range(length):
        cnt = 0
        for j in range(len(want)):
            if discount[i:i + 10].count(want[j]) >= number[j]:
                cnt += 1
        if cnt == len(want):
            answer += 1

    return answer