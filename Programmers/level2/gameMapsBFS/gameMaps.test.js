import { solution } from './gameMaps.js';

describe('gameMaps TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]];
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 11', (done) => {
    const element1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]];
    expect(solution(element1)).toEqual(11);
    done();
  });

  test('should return -1', (done) => {
    const element1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]];
    expect(solution(element1)).toEqual(-1);
    done();
  });

});