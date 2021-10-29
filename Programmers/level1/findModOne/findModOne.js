// https://programmers.co.kr/learn/courses/30/lessons/87389?language=javascript

export const solution = (n) => {
    let answer = 0;
    for(let i = 1; i < n; i++){
        if(n % i === 1){
            answer += i;
            break;
        }
    }
    return answer;
}