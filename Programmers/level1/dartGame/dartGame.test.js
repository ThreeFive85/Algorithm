import { solution } from './dartGame.js';

describe('dartGame TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = "1S2D*3T";
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 37', (done) => {
    const element1 = "1S2D*3T";
    expect(solution(element1)).toEqual(37);
    done();
  });

  test('should return 23', (done) => {
    const element1 = "1S*2T*3S";
    expect(solution(element1)).toEqual(23);
    done();
  });

  test('should return 5', (done) => {
    const element1 = "1D#2S*3S";
    expect(solution(element1)).toEqual(5);
    done();
  });
});