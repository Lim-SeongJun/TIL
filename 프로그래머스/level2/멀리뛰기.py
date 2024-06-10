def solution(n):
    answer = 0
    N = [0]*(n+1)
    N[1]=1
    N[2]=2
    if n>2:
        for i in range(2,n):
            N[i+1] = N[i-1]+N[i]
    return N[n]%1234567
# 1일때 1
# 2일때 2
# 3일때 3
# 4일때 5
# 5일때 8개
if __name__ == "__main__":
    print(solution(4))