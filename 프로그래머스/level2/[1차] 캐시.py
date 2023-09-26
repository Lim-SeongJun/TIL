def solution(cacheSize, cities):
    answer = 0
    cities = list(map(lambda x: x.lower(),cities))
    cache = []
    if cacheSize != 0:
        for ref in cities:
            if not ref in cache:
                if len(cache) < cacheSize:
                    cache.append(ref)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(ref)
                    answer += 5
            else:
                cache.pop(cache.index(ref))
                cache.append(ref)
                answer+=1
    else:
        return len(cities)*5
    return answer