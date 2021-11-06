export const solution = (brown, yellow) => {
    let answer = [];
    let total = brown + yellow;
    for(let i = 1; i < total+1; i++){
        if(total % i === 0){
            let x = total / i;
            let y = i;
            if(x < y){
                break;
            } else {
                answer.push([x,y])
            }
        }
    }
    // console.log(answer)
    for(let i = 0; i < answer.length; i++){
        if(answer[i][0] * 2 + answer[i][1] * 2 - 4 === brown){
            return answer[i];
        }
    }
}