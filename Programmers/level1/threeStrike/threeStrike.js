// https://programmers.co.kr/learn/courses/30/lessons/68935?language=javascript

export const solution = (n) => {
    let answer = 0;
    let change = parseInt(n).toString(3);
    for(let i = 0; i < change.length; i++){
        answer += Number(change[i]) * 3**i
    }
    return answer;
}