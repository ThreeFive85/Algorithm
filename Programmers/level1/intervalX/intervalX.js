// https://programmers.co.kr/learn/courses/30/lessons/12954?language=javascript

export const solution = (x, n) => {
    let answer = [];
    for(let i = 1; i < n+1; i++){
        answer.push(x*i)
    }
    return answer;
}