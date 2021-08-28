import { solution } from './maxminLottos.js';

describe('maxminLottos TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = [44, 1, 0, 0, 31, 25]
    const element2 = [31, 10, 45, 1, 6, 19]
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [3, 5]', (done) => {
    const element1 = [44, 1, 0, 0, 31, 25]
    const element2 = [31, 10, 45, 1, 6, 19]
    expect(solution(element1, element2)).toEqual([3, 5]);
    done();
  });

  test('should return [1, 6]', (done) => {
    const element1 = [0, 0, 0, 0, 0, 0]
    const element2 = [38, 19, 20, 40, 15, 25]
    expect(solution(element1, element2)).toEqual([1, 6]);
    done();
  });
  
  test('should return [1, 1]', (done) => {
    const element1 = [45, 4, 35, 20, 3, 9]
    const element2 = [20, 9, 3, 45, 4, 35]
    expect(solution(element1, element2)).toEqual([1, 1]);
    done();
  });
  
});
