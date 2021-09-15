// https://programmers.co.kr/learn/courses/30/lessons/42885?language=javascript

export const solution = (people, limit) => {
    let answer = 0;
    let sort_peo = people.sort((a,b) => b - a);
    let left = 0;
    let right = people.length - 1;
    while(left < right){
        let weight = sort_peo[left] + sort_peo[right];
        if( weight > limit ){
            left++;
        } else {
            left++;
            right--;
        }
        answer++;
    }
    if(left === right){
        answer++;
    }
    return answer;
}

// people을 내림차순으로 정렬한다.
// 첫번째 수(가장 큰 수)와 마지막 수(가장 작은 수)를 더한 값을 구한다.
//  limit을 넘는다면 (첫번째 수만 배에 태우기 때문에) 다음 수로 향하도록 l++ 한다.
//  limit을 넘지 않으면 (첫번째 수와 마지막 수를 배에 태우기 때문에) 양 끝에서 다음 수로 향하도록 l++, r-- 한다.
// 혼자 탄 배 추가를 위해 answer++
// 함께 탄 배 추가를 위해 answer++
// 만약 people[l] == people[r] 즉, 계산되지 않은 마지막 숫자가 남았다면, 이 숫자 혼자 타는 배를 추가하기 위해 answer++ 한다.