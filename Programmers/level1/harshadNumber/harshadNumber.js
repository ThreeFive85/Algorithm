// https://programmers.co.kr/learn/courses/30/lessons/12947?language=javascript

export const solution = (x) => {
    let answer = true;
    let sum = 0;
    String(x).split('').forEach(char => sum += Number(char) );
    if(x % sum !== 0) return false;
    return answer;
}