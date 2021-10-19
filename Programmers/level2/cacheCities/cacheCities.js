// https://programmers.co.kr/learn/courses/30/lessons/17680?language=javascript

export const solution = (cacheSize, cities) => {
    let answer = 0;
    let cache = [];
    if(cacheSize === 0){
        return cities.length * 5
    }
    cities.forEach(el => {
        el = el.toLowerCase();
        let idx = cache.indexOf(el);
        if(idx > -1){
            cache.splice(idx, 1);
            answer += 1;
        } else {
            if(cache.length >= cacheSize){
                cache.shift();
            }
            answer += 5;
        }
        cache.push(el);
    })
    return answer;
}