import { solution } from './toInteger.js';

describe('toInteger TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = "12"
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 12', (done) => {
    const element1 = "12"
    expect(solution(element1)).toEqual(12);
    done();
  });

  test('should return -12', (done) => {
    const element1 = "-12"
    expect(solution(element1)).toEqual(-12);
    done();
  });

  test('should return 1', (done) => {
    const element1 = "1"
    expect(solution(element1)).toEqual(1);
    done();
  });
});