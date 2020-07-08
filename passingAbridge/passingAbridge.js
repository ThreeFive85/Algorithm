/*
문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42583
*/

const passingAbridge = (bridge_length, weight, truck_weights) => {
  let count = 0;
  let bridge = [];
  let bridgeSum = 0;

  for (let i = 0; i < bridge_length - 1; i++) {
    bridge.push(0);
  }

  let now_truck = truck_weights.shift();

  bridge.unshift(now_truck);
  // console.log(bridge);
  bridgeSum += now_truck;
  count++;

  while (bridgeSum) {
    bridgeSum -= bridge.pop();
    now_truck = truck_weights.shift();

    if (now_truck + bridgeSum <= weight) {
      bridge.unshift(now_truck);
      bridgeSum += now_truck;
    } else {
      bridge.unshift(0);
      truck_weights.unshift(now_truck);
    }
    count++;
  }
  // console.log(count);
  return count;
};

// passingAbridge(2, 10, [7, 4, 5, 6]);
export default passingAbridge;

// 다리길이가 2, 다리는 트럭무게 총 합 10을 견딜수 있다. 트럭은 [7,4,5,6]무게를 가지고 있다.
// 7무게의 트럭이 다리에 들어가면 1초가 흐르고 다리의 공간은 한 자리가 남는다.
// 다리에 트럭이 들어갈 수 있는 자리가 있지만 다음은 4무게의 트럭이므로 견딜수 있는 무게10을 넘는다.
// [],[],[7,4,5,6]
// [],[7,0],[4,5,6] 1초
// [7],[4,0],[5,6] 2초, 3초
// [7],[4,5],[6] 4초
// [7,4],[5,0],[6] 5초
// [7,4,5],[6,0],[] 6초, 7초
// [7,4,5,6],[],[], 8초
