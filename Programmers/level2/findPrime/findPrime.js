// 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42839?language=javascript

export const solution = (numbers) => {
    var answer = 0;
    let n = numbers.split('')
    let nums = new Set();
    permutation(n,'');
    
    function permutation(a,s){
        if(s.length > 0){
            if(nums.has(Number(s)) === false){
                nums.add(Number(s));
                if(primeTester(Number(s))){
                    answer++;
                }
            }
        }
        if(a.length > 0){
            for(let i = 0; i < a.length; i++){
                let t = a.slice(0);
                console.log("t : ", t)
                t.splice(i, 1);
                permutation(t, s + a[i])
            }
        }
    }
    function primeTester(n){
        if (typeof n !== "number" || n < 1 || n % 1 !== 0) {
    return false;
  }
  if (n === 1) {
    return false;
  }
  let num = Math.sqrt(n);
  for (let i = 2; i <= num; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
    }
    console.log(nums)
    return answer;
}