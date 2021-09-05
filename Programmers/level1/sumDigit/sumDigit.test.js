import { solution } from './sumDigit.js';

describe('sumDigit TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 123
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 6', (done) => {
    const element1 = 123
    expect(solution(element1)).toEqual(6);
    done();
  });

  test('should return 0', (done) => {
    const element1 = 0
    expect(solution(element1)).toEqual(0);
    done();
  });

  test('should return 3', (done) => {
    const element1 = 12
    expect(solution(element1)).toEqual(3);
    done();
  });
});