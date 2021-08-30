// https://programmers.co.kr/learn/courses/30/lessons/12948?language=javascript

export const solution = (phone_number) => {
    
    return phone_number.slice(0, -4).split('').map(el => el = '*').join('') + phone_number.slice(-4);
}