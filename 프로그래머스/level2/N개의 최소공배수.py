def LCM(a,b):
    lcm = 0
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            lcm = i
            break
    return i
def solution(arr):
    arr.sort()
    answer = LCM(arr[0],arr[1])
    for i in range(len(arr)-1):
        answer = LCM(answer,arr[i+1])
    return answer