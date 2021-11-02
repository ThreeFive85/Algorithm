// https://programmers.co.kr/learn/courses/30/lessons/86491?language=javascript

export const solution = (sizes) => {
    let w = Math.max(...wh(0, sizes));
    let h = Math.max(...wh(1, sizes))
    return w * h;
}

const wh = (maxmin, arr) => { 
    let temp = []
    if(maxmin === 0){
        arr.forEach(el => {
            temp.push(Math.max(el[0],el[1]))
        })
    } else {
        arr.forEach(el => {
            temp.push(Math.min(el[0],el[1]))
        })
    }
    // console.log(temp)
    return temp;
}