import { solution } from './getAverage.js';

describe('getAverage TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [1,2,3,4]
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 2.5', (done) => {
    const element1 = [1,2,3,4]
    expect(solution(element1)).toEqual(2.5);
    done();
  });

  test('should return 5', (done) => {
    const element1 = [5,5]
    expect(solution(element1)).toEqual(5);
    done();
  });

  test('should return 0', (done) => {
    const element1 = [0,0]
    expect(solution(element1)).toEqual(0);
    done();
  });
});
