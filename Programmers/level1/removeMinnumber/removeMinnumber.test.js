import { solution } from './removeMinnumber.js';

describe('removeMinnumber TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = [4,3,2,1]
    expect(typeof solution(element1)).toEqual('object');
    done();
  });

  test('should return [4,3,2]', (done) => {
    const element1 = [4,3,2,1]
    expect(solution(element1)).toEqual([4,3,2]);
    done();
  });

  test('should return [-1]', (done) => {
    const element1 = [10]
    expect(solution(element1)).toEqual([-1]);
    done();
  });

  test('should return [5,12,23]', (done) => {
    const element1 = [5,12,1,23]
    expect(solution(element1)).toEqual([5,12,23]);
    done();
  });
});