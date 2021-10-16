import { solution } from './threeStrike.js';

describe('threeStrike TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 45;
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 7', (done) => {
    const element1 = 45;
    expect(solution(element1)).toEqual(7);
    done();
  });

  test('should return 229', (done) => {
    const element1 = 125;
    expect(solution(element1)).toEqual(229);
    done();
  });

});