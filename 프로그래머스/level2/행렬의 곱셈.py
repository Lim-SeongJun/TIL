def solution(arr1, arr2):
    answer = []
    num = 0
    cnt = []
    for i in arr1:
        for j in zip(*arr2):
            for a,b in zip(i,j):
                num+=a*b
            cnt.append(num)
            num = 0
        answer.append(cnt)
        cnt = []
    '''answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]'''
    '''for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            for z in range(len(arr2[0])):
                answer[i][z] += arr1[i][j]*arr2[j][z]'''
    return answer