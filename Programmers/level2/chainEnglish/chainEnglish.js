// https://programmers.co.kr/learn/courses/30/lessons/12981?language=javascript

export const solution = (n, words) => {
    
    let stack = [];
    let player = 1;
    let turn = 1;
    
    while(words.length > 1){
        stack.push(words.shift())
        player += 1;
        if(stack.length % n === 0){
            player = 1;
            turn += 1;
        }
        if(stack[stack.length-1][stack[stack.length-1].length-1] !== words[0][0]){
            return [player, turn];
        }else if(stack.includes(words[0])){
            return [player, turn];
        } 
    } 
    
    return [0,0]
}