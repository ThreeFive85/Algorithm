import { solution } from './noRepeatNumbers.js';

describe('noRepeatNumbers TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = [1,1,3,3,0,1,1]
    expect(typeof solution(element1)).toEqual('object');
    done();
  });

  test('should return [1,3,0,1]', (done) => {
    const element1 = [1,1,3,3,0,1,1]
    expect(solution(element1)).toEqual([1,3,0,1]);
    done();
  });

  test('should return [4,3]', (done) => {
    const element1 = [4,4,4,3,3]
    expect(solution(element1)).toEqual([4,3]);
    done();
  });

  test('should return [1,1]', (done) => {
    const element1 = [1,1]
    expect(solution(element1)).toEqual([1]);
    done();
  });
});