def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            idx = cache.index(city)
            cache = cache[:idx] + cache[idx + 1:] + [cache[idx]]
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache = cache[1:] + [city]
            answer += 5
    if cacheSize == 0:
        answer = len(cities) * 5
    return answer


print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(0, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
