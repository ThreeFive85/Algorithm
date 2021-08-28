// https://programmers.co.kr/learn/courses/30/lessons/77484?language=javascript

export const solution = (lottos, win_nums) => {

    let prize = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 };
    let max_cnt = 0;
    let min_cnt = 0;
    lottos.forEach(el => {
        if(win_nums.includes(el)){
            max_cnt += 1;
            min_cnt += 1;
        } else if(el === 0){
            max_cnt += 1;
        }
    })
    let answer = [prize[max_cnt], prize[min_cnt]]
    return answer;
}