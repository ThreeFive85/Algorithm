// https://programmers.co.kr/learn/courses/30/lessons/12978?language=javascript
// 참고블로그 : https://msko.tistory.com/9

export const solution = (N, road, K) => {
    
    const dis = Array(N+1).fill(Infinity);
    // console.log(dis)
    const adj = Array.from({length:N+1}, () => []);
    // console.log(adj)
    road.forEach(([a,b,c]) => {
        adj[a].push({to: b, time: c});
        adj[b].push({to: a, time: c});
    });
    // console.log(adj)
    const p = [{to: 1, time: 0}];
    dis[1] = 0
    
    while(p.length){
        let {to, time} = p.pop();
        adj[to].forEach((next) => {
            if(dis[next.to] > dis[to] + next.time){
                dis[next.to] = dis[to] + next.time;
                p.push(next);
            }
        })
    }

    return dis.filter((item) => item <= K).length;
}