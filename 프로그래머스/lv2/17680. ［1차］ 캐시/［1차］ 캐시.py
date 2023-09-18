def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    for city in cities:
        city = city.upper()
        if city not in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer