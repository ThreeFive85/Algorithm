function solution(w, h) {
    let gcd = 1;
    let min = Math.min(w,h);
    
    for(let i = min; i > 0; i--){
        if(w % i === 0 && h % i === 0){
            gcd = i
            break;
        }
    }
    return w * h - (w + h - gcd)
}