import { solution } from './makeListReverseInt.js';

describe('makeListReverseInt TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 12345
    expect(typeof solution(element1)).toEqual('object');
    done();
  });

  test('should return [5,4,3,2,1]', (done) => {
    const element1 = 12345
    expect(solution(element1)).toEqual([5,4,3,2,1]);
    done();
  });

  test('should return [1,2,3,4,5]', (done) => {
    const element1 = 54321
    expect(solution(element1)).toEqual([1,2,3,4,5]);
    done();
  });

  test('should return [1,2]', (done) => {
    const element1 = 12
    expect(solution(element1)).toEqual([2,1]);
    done();
  });
});
