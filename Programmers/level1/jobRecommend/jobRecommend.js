// https://programmers.co.kr/learn/courses/30/lessons/84325?language=javascript

export const solution = (table, languages, preference) => {
    let answer = [];
    for(let i = 0; i < table.length; i++){
        let job = table[i].split(' ')
        let num = 0;
        for(let j = 0; j < languages.length; j++){
            if(job.includes(languages[j])){
                num += preference[j] * (6-job.indexOf(languages[j]));
            } else {
                num += 0;
            }
        }
        let obj = { job : job[0], num : num}
        answer.push(obj);
    }
    answer.sort((a,b) => {
        if(a.num < b.num) return 1;
        if(a.num > b.num) return -1;
        if(a.num === b.num){
            let nameA = a.job.toUpperCase(); // ignore upper and lowercase
            let nameB = b.job.toUpperCase(); // ignore upper and lowercase
            if (nameA < nameB) {
                return -1;
              }
            if (nameA > nameB) {
                return 1;
              }
              // 이름이 같을 경우
            return 0;
                }
            });
    // console.log(answer)
    return answer[0].job;
}