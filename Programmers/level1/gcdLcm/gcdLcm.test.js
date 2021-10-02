import { solution } from './gcdLcm.js';

describe('gcdLcm TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 3
    const element2 = 12
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [3,12]', (done) => {
    const element1 = 3
    const element2 = 12
    expect(solution(element1, element2)).toEqual([3,12]);
    done();
  });

  test('should return [1,10]', (done) => {
    const element1 = 2
    const element2 = 5
    expect(solution(element1, element2)).toEqual([1,10]);
    done();
  });
});
