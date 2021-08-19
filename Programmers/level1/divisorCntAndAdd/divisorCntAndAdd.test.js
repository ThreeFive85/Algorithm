import { solution } from './divisorCntAndAdd.js';

describe('divisorCntAndAdd TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 13
    const element2 = 17
    expect(typeof solution(element1, element2)).toEqual('number');
    done();
  });

  test('should return 43', (done) => {
    const element1 = 13
    const element2 = 17
    expect(solution(element1, element2)).toEqual(43);
    done();
  });

  test('should return 52', (done) => {
    const element1 = 24
    const element2 = 27
    expect(solution(element1, element2)).toEqual(52);
    done();
  });
});
