// https://programmers.co.kr/learn/courses/30/lessons/12950?language=javascript

export const solution = (arr1, arr2) => {
    let answer = [];
    for(let i = 0; i < arr1.length; i++){
        let arr = [];
        for(let j = 0; j < arr1[0].length; j++){
            arr.push(arr1[i][j]+arr2[i][j]);
        }
        answer.push(arr);
    }
    return answer;
};