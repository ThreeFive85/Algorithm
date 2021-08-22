// https://programmers.co.kr/learn/courses/30/lessons/12944?language=javascript

export const solution = (arr) => {
    let answer = arr.reduce((prev, curr) => prev + curr ) / arr.length;
    return answer;
}