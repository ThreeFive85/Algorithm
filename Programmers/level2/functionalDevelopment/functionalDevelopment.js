// https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript

export const solution = (progresses, speeds) => {
    let answer = [];
    
    while(speeds.length > 0){
        for(let i = 0; i < speeds.length; i++){
            if(progresses[i] < 100){
                progresses[i] += speeds[i];
            }
        }
        let deployCount = 0;
        while(progresses[0] >= 100){
            progresses.shift();
            speeds.shift();
            deployCount++
        }
        if(deployCount > 0){
            answer.push(deployCount)
        }
    }
    return answer;
}