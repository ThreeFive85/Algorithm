// https://programmers.co.kr/learn/courses/30/lessons/12985?language=javascript

export const solution = (n,a,b) => {
    let answer = 0;

    while(a != b){
        answer += 1;
        a = parseInt((a+1)/2)
        b = parseInt((b+1)/2)
    }

    return answer;
}