// https://programmers.co.kr/learn/courses/30/lessons/12933?language=javascript

export const solution = (n) => {
    
    let sort = String(n).split('').map(element => Number(element)).sort((a,b) => b - a).join('')
    
    return Number(sort);
}