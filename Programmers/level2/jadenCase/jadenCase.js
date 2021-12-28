// https://programmers.co.kr/learn/courses/30/lessons/12951?language=javascript

export const solution = (s) => {
    var answer = '';
    if(s[0] !== ' '){
          answer += s[0].toUpperCase();  
        }
    for(let i = 1; i < s.length; i++){
        if(s[i-1] === ' '){
            answer += s[i].toUpperCase();
        } else {
            answer += s[i].toLowerCase();
        }
    }
    return answer;
}