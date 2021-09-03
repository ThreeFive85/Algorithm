import { solution } from './stringNumberAndAlpha.js';

describe('stringNumberAndAlpha TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = "1zerotwozero3"
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 10203', (done) => {
    const element1 = "1zerotwozero3"
    expect(solution(element1)).toEqual(10203);
    done();
  });

  test('should return 1478', (done) => {
    const element1 = "one4seveneight"
    expect(solution(element1)).toEqual(1478);
    done();
  });

  test('should return 234567', (done) => {
    const element1 = "23four5six7"
    expect(solution(element1)).toEqual(234567);
    done();
  });
});