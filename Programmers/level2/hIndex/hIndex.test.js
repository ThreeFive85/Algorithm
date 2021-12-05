import { solution } from './hIndex.js';

describe('hIndex TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [3, 0, 6, 1, 5];
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 3', (done) => {
    const element1 = [3, 0, 6, 1, 5];
    expect(solution(element1)).toEqual(3);
    done();
  });

  test('should return 3', (done) => {
    const element1 = [2, 1, 7, 9, 6];
    expect(solution(element1)).toEqual(3);
    done();
  });
  
});