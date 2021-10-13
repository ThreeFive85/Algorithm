// https://programmers.co.kr/learn/courses/30/lessons/42578?language=javascript

export const solution = (clothes) => {
    // var answer = 1;
    // let obj = {};
    // for(let i = 0; i < clothes.length; i++){
    //     obj[clothes[i][1]] = (obj[clothes[i][1]] || 1) + 1
    // }
    // console.log(obj)
    // for(let z in obj){
    //     answer *= obj[z]
    // }
    // return answer - 1;
    return Object.values(clothes.reduce((obj,z) => {
        obj[z[1]] = obj[z[1]] ? obj[z[1]] + 1 : 1;
        console.log(obj)
        return obj
    }, {})).reduce((a,b) => a*(b+1),1)-1;
}