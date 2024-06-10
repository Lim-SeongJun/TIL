def solution(prices):
    answer = [0] * len(prices)
    stack = [[prices[-1], 0]]

    for i in range(len(prices) - 2, -1, -1):
        price = prices[i]

        popCount = 1
        while stack and price <= stack[-1][0]:
            _ , count = stack.pop()
            popCount += count
        stack.append([price, popCount])
        answer[i] = popCount

    return answer