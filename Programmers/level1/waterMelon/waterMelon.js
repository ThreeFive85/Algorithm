// https://programmers.co.kr/learn/courses/30/lessons/12922?language=javascript

export const solution = (n) => {
    var answer = '수박'.repeat(n);
    return answer.slice(0, -n);
}