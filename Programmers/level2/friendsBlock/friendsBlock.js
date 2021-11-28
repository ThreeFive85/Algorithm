export const solution = (m,n,board) => {
    let answer = 0;
    board = board.map(b => b.split(''));
    // console.log(board)
    while(true){
        let block = [];
        // find block index
        for(let i = 1; i < m; i++){
            for(let j = 1; j < n; j++){
                if(board[i][j] && board[i][j] === board[i-1][j] && board[i][j] === board[i][j-1]
                    && board[i][j] === board[i-1][j-1]){
                        block.push([i, j])
                    }
                }
            }
        // console.log([].concat(...board).filter(e => !e));
        if(!block.length) return [].concat(...board).filter(e => !e).length;

        // change same blocks with 0
        block.forEach(e => {
            board[e[0]][e[1]] = 0;
            board[e[0]-1][e[1]] = 0;
            board[e[0]][e[1]-1] = 0;
            board[e[0]-1][e[1]-1] = 0;
        })

        // resort
        for (let i = m - 1; i > 0; i--) {
            if (! board[i].some(v => ! v)) continue;

            for (let j = 0; j < n; j++) {
                for (let k = i - 1; k >= 0 && ! board[i][j]; k--) {
                    if (board[k][j]) {
                        board[i][j] = board[k][j];
                        board[k][j] = 0;
                        break;
                    }
                }
            }
        }
    }
};

// solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]) 
// solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) 