// https://programmers.co.kr/learn/courses/30/lessons/12932?language=javascript

export const solution = (n) => {
    let answer = String(n).split('').reverse().map(element => Number(element))
    // console.log(answer)
    return answer;
}