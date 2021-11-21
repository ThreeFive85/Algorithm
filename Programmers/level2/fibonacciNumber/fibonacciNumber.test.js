import { solution } from './fibonacciNumber.js';

describe('fibonacciNumber TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 15;
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 2', (done) => {
    const element1 = 3;
    expect(solution(element1)).toEqual(2);
    done();
  });

  test('should return 5', (done) => {
    const element1 = 5;
    expect(solution(element1)).toEqual(5);
    done();
  });

});