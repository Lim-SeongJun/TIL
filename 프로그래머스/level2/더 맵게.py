import heapq as hp


def solution(scoville, K):
    hp.heapify(scoville)
    count = 0
    while scoville[0] < K:
        count += 1
        hp.heappush(scoville, hp.heappop(scoville) + hp.heappop(scoville) * 2)

        if (len(scoville) == 2) and (scoville[0] + scoville[1] * 2) < K:
            return -1

    return count