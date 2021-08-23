import { solution } from './harshadNumber.js';

describe('harshadNumber TEST', () => {
  test('should return type of result "boolean"', (done) => {
    const element1 = 18
    expect(typeof solution(element1)).toEqual('boolean');
    done();
  });

  test('should return true', (done) => {
    const element1 = 18
    expect(solution(element1)).toEqual(true);
    done();
  });

  test('should return false', (done) => {
    const element1 = 19
    expect(solution(element1)).toEqual(false);
    done();
  });

  test('should return true', (done) => {
    const element1 = 10
    expect(solution(element1)).toEqual(true);
    done();
  });
});
