import { solution } from './sumMatrix.js';

describe('sumMatrix TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = [[1,2],[2,3]];
    const element2 = [[3,4],[5,6]];
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return [[4,6],[7,9]]', (done) => {
    const element1 = [[1,2],[2,3]];
    const element2 = [[3,4],[5,6]];
    expect(solution(element1, element2)).toEqual([[4,6],[7,9]]);
    done();
  });

  test('should return [[4],[6]]', (done) => {
    const element1 = [[1],[2]];
    const element2 = [[3],[4]];
    expect(solution(element1, element2)).toEqual([[4],[6]]);
    done();
  });
  
  test('should return [[0,0,0],[0,0,0]]', (done) => {
    const element1 = [[0,0,0],[0,0,0]];
    const element2 = [[0,0,0],[0,0,0]];
    expect(solution(element1, element2)).toEqual([[0,0,0],[0,0,0]]);
    done();
  });
  
});
