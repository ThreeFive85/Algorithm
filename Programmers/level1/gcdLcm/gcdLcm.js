// https://programmers.co.kr/learn/courses/30/lessons/12940?language=javascript

export const solution = (n, m) => {
    let answer = [];
    let c = Math.max(n, m);
    let d = Math.min(n, m);
    
    answer[0] = gcd(n, m);
    answer[1] = n * m / gcd(n, m);

    return answer;
};

const gcd = (min, max) => {
    return (min % max) === 0 ? max : gcd(max, min % max) 
}

// solution(1, 10)