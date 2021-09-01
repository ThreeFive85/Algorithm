// https://programmers.co.kr/learn/courses/30/lessons/12935?language=javascript

export const solution = (arr) => {
    let index = Math.min(...arr);
    arr.splice(arr.indexOf(index), 1);
    if(arr.length === 0) return [-1];
    return arr;
}