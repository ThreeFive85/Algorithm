// https://programmers.co.kr/learn/courses/30/lessons/12905?language=javascript

export const solution = (board) => {

    let m = board.length;
    let n = board[0].length;
    
    for(let i = 1; i < m; i++){
        for(let j = 1; j < n; j++){
            if(board[i][j] === 1){
               board[i][j] = Math.min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1 
            }
        }
    }
    console.log(board)
    let max = 0;
    board.forEach(el => {
        if(Math.max(...el) > max){
            max = Math.max(...el); 
        }
    })

    return max**2;
}
