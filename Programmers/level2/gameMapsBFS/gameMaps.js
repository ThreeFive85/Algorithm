// https://programmers.co.kr/learn/courses/30/lessons/1844?language=javascript

export const solution = (maps) => {
    const dx = [-1,1,0,0];
    const dy = [0,0,-1,1];
    let que = [[0,0]];
    while(que.length > 0){
        let popQue = que.shift();
        let x = popQue[0];
        // console.log(x)
        let y = popQue[1];
        for(let i = 0; i < 4; i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            if(nx < 0 || nx >= maps.length || ny < 0 || ny >= maps[0].length){
                continue
            };
            if(maps[nx][ny] === 0){
                continue
            };
            if(maps[nx][ny] === 1){
                maps[nx][ny] = maps[x][y] + 1
                que.push([nx,ny])
            }
        }
    }
    // console.log(maps)
    if(maps[maps.length-1][maps[0].length-1] === 1){
        return -1;
    }
    return maps[maps.length-1][maps[0].length-1];
}

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])