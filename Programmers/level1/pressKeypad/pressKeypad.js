// https://programmers.co.kr/learn/courses/30/lessons/67256?language=javascript

export const solution = (numbers, hand) => {
    let answer = '';
    let location = {
        "1": [0,0], "2": [0,1], "3": [0,2],
        "4": [1,0], "5": [1,1], "6": [1,2],
        "7": [2,0], "8": [2,1], "9": [2,2],
        "*": [3,0], "0": [3,1], "#": [3,2],
    }
    let right = '#';
    let left = '*';
    numbers.forEach(el => {
        if(el === 1 || el === 4 || el === 7 ){
            answer += 'L';
            left = String(el);
        } else if (el === 3 || el === 6 || el === 9){
            answer += 'R';
            right = String(el);
        } else if (el === 2 || el === 5 || el === 8 || el === 0){
            let l_dis = Math.abs(location[left][0] - location[String(el)][0]) + 
                        Math.abs(location[left][1] - location[String(el)][1]);
            let r_dis = Math.abs(location[right][0] - location[String(el)][0]) + 
                        Math.abs(location[right][1] - location[String(el)][1]);
            if(l_dis < r_dis){
                answer += 'L';
                left = String(el);
            } else if(l_dis > r_dis){
                answer += 'R';
                right = String(el);
            } else if(l_dis === r_dis){
                if(hand === 'left'){
                    answer += 'L';
                    left = String(el);
                } else {
                    answer += 'R';
                    right = String(el);
                }
            }
        }
    })
    
    return answer;
}