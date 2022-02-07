export const solution = (n, times) => {
    let answer = 0;
    let left = 1;
    let right = Math.max(...times) * n;
    // console.log(right)

    while(left < right){
        let mid = parseInt((left+right)/2);
        let cnt = 0;
        for(let time of times){
            cnt += parseInt(mid/time); 
        }
        if(cnt >= n){
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    answer = left;
    return answer;
}