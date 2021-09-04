// https://programmers.co.kr/learn/courses/30/lessons/12917?language=javascript

export const solution = (s) => {
    let answer = s.split('').sort((a,b) => {
        if (a > b) return -1;
        if (b > a) return 1;
        return 0;
    }).join('');
    return answer;
}