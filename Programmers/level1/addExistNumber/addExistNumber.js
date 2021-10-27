// https://programmers.co.kr/learn/courses/30/lessons/86051?language=javascript

export const solution = (numbers) => {
    var answer = 45;
    return answer - numbers.reduce((a, b) => a + b);
}