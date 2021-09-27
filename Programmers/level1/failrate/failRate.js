// https://programmers.co.kr/learn/courses/30/lessons/42889?language=javascript

export const solution = (N, stages) => {
    let answer = {};
    let users = stages.length;
    for(let i = 1; i < N+1; i++){
        if(users !== 0){
            answer[i] = stages.filter(el => el === i).length / users;
            users -= stages.filter(el => el === i).length;
        } else {
            answer[i] = 0;
        }
    }
    // console.log(answer)
    let sortArr = []
    for(let fail in answer){
        sortArr.push([fail, answer[fail]])
    }
    sortArr.sort((a, b) => {
        if(a[1] < b[1]) return 1;
        if(a[1] > b[1]) return -1;
        if(a[1] === b[1]) return 0;
    })
    let result = [];
    // console.log(sortArr)
    sortArr.map(el => result.push(Number(el[0])))
    // console.log(result)
    return result;
}
