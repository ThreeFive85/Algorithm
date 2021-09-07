// https://programmers.co.kr/learn/courses/30/lessons/12928?language=javascript

export const solution = (n) => {
    let answer = 0;
    for(let i = 1; i < n+1; i++){
        if(n % i === 0) answer += i;
    }
    return answer;
};