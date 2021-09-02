// https://programmers.co.kr/learn/courses/30/lessons/12930?language=javascript

export const solution = (s) => {
    let answer = '';
    let idx = 0;
    for(let i = 0; i < s.length; i++){
        if(s[i] === ' '){
            answer += ' ';
            idx = 0;
        } else if(idx % 2 === 0){
            answer += s[i].toUpperCase();
            idx += 1;
        } else {
            answer += s[i].toLowerCase();
            idx += 1;
        }
    }
    return answer;
}