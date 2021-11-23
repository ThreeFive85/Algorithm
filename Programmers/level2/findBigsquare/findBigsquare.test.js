import { solution } from './findBigsquare.js';

describe('findBigsquare TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]];
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 9', (done) => {
    const element1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]];
    expect(solution(element1)).toEqual(9);
    done();
  });

  test('should return 4', (done) => {
    const element1 = [[0,0,1,1],[1,1,1,1]];
    expect(solution(element1)).toEqual(4);
    done();
  });

});