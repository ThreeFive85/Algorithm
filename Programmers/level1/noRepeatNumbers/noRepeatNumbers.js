// https://programmers.co.kr/learn/courses/30/lessons/12906?language=javascript

export const solution = (arr) => {
    let answer = [];

    for(let i = 0; i < arr.length; i++){
        if(arr[i] === answer[answer.length-1]) continue;
         answer.push(arr[i]);  
    }
    
    return answer;
}