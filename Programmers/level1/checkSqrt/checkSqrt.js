// https://programmers.co.kr/learn/courses/30/lessons/12934?language=javascript

export const solution = (n) => {
    let answer = 0;
    if(n % Math.sqrt(n) === 0){
        answer += (Math.sqrt(n)+1) ** 2
    }else{
        return -1;
    }
    return answer;
}