# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17680
# 참고 블로그 : https://geonlee.tistory.com/102

def solution(cacheSize, cities):
    cache = []
    cnt = 0
    if cacheSize == 0:
        return len(cities) * 5
    while cities:
        city = cities.pop().lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            cnt += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
                cnt += 5
            else:
                del cache[0]
                cache.append(city)
                cnt += 5
    print(cache)
    print(cnt)
    return cnt
