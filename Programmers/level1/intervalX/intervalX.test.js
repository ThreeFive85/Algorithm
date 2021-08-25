import { solution } from './intervalX.js';

describe('intervalX TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 2
    const element2 = 5
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [2,4,6,8,10]', (done) => {
    const element1 = 2
    const element2 = 5
    expect(solution(element1, element2)).toEqual([2,4,6,8,10]);
    done();
  });

  test('should return [4,8,12]', (done) => {
    const element1 = 4
    const element2 = 3
    expect(solution(element1, element2)).toEqual([4,8,12]);
    done();
  });

  test('should return [-4,-8]', (done) => {
    const element1 = -4
    const element2 = 2
    expect(solution(element1, element2)).toEqual([-4, -8]);
    done();
  });
});
