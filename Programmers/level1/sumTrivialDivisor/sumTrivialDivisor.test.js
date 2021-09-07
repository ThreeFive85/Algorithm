import { solution } from './sumTrivialDivisor.js';

describe('sumTrivialDivisor TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 12
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 28', (done) => {
    const element1 = 12
    expect(solution(element1)).toEqual(28);
    done();
  });

  test('should return 6', (done) => {
    const element1 = 5
    expect(solution(element1)).toEqual(6);
    done();
  });

  test('should return 1', (done) => {
    const element1 = 1
    expect(solution(element1)).toEqual(1);
    done();
  });
});