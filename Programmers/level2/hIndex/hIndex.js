export const solution = (citations) => {
    var answer = 0;
    citations.sort((a,b) => {
        return b-a
    })
    let idx = 1;
    let arr = [];
    citations.forEach(c => {
        arr.push(Math.min(idx,c))
        idx += 1;
    })
    // console.log(arr)
    return Math.max(...arr)
}