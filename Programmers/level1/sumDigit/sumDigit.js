// https://programmers.co.kr/learn/courses/30/lessons/12931?language=javascript#

export const solution = (n) => {
    let answer = String(n).split('').map(el => Number(el)).reduce((acc, cur) => acc + cur);
    return answer;
};