// https://programmers.co.kr/learn/courses/30/lessons/12926?language=javascript

export const solution = (s, n) => {
    let answer = '';
    let lower = 'abcdefghijklmnopqrstuvwxyz';
    let upper = lower.toUpperCase();
    for(let i = 0; i < s.length; i++){
        if(s[i] === ' '){
            answer += s[i];
        } else if(s[i] == s[i].toUpperCase()){
            let idx = upper.indexOf(s[i]) + n;
            if(idx > 25){
                idx = idx % 26;
            };
            answer += upper[idx]
        } else if(s[i] == s[i].toLowerCase()){
            let idx = lower.indexOf(s[i]) + n;
            if(idx > 25){
                idx = idx % 26;
            };
            answer += lower[idx]
        } 
    }
    return answer;
}