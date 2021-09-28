import { solution } from './failRate.js';

describe('failRate TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = 5;
    const element2 = [2, 1, 2, 6, 2, 4, 3, 3];
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [3,4,2,1,5]', (done) => {
    const element1 = 5;
    const element2 = [2, 1, 2, 6, 2, 4, 3, 3];
    expect(solution(element1, element2)).toEqual([3,4,2,1,5]);
    done();
  });

  test('should return [4,1,2,3]', (done) => {
    const element1 = 4;
    const element2 = [4,4,4,4,4];
    expect(solution(element1, element2)).toEqual([4,1,2,3]);
    done();
  });
});
