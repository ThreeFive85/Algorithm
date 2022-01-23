import { solution } from './delivery.js';

describe('delivery TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 5;
    const element2 = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]];
    const element3 = 3;
    expect(typeof solution(element1, element2, element3)).toEqual('number');
    done();
  });

  test('should return 4', (done) => {
    const element1 = 5;
    const element2 = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]];
    const element3 = 3;
    expect(solution(element1,element2,element3)).toEqual(4);
    done();
  });

  test('should return 4', (done) => {
    const element1 = 6;
    const element2 = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]];
    const element3 = 4;
    expect(solution(element1,element2,element3)).toEqual(4);
    done();
  });

});