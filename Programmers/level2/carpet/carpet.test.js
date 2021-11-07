import { solution } from './carpet.js';

describe('carpet TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 10;
    const element2 = 2;
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [4,3]', (done) => {
    const element1 = 10;
    const element2 = 2;
    expect(solution(element1,element2)).toEqual([4,3]);
    done();
  });

  test('should return [3,3]', (done) => {
    const element1 = 8;
    const element2 = 1;
    expect(solution(element1,element2)).toEqual([3,3]);
    done();
  });

});