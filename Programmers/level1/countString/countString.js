// https://programmers.co.kr/learn/courses/30/lessons/12916?language=javascript

export const solution = (s) => {
    let p = s.toLowerCase().split('').filter(element => element === 'p').length;
    let y = s.toLowerCase().split('').filter(element => element === 'y').length;
    
    if(p === y) return true;
    return false;
}