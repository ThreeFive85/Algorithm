import { solution } from './insufficientAmount.js';

describe('insufficientAmount TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 3;
    const element2 = 20;
    const element3 = 4;
    expect(typeof solution(element1, element2, element3)).toEqual('number');
    done();
  });

  test('should return 10', (done) => {
    const element1 = 3;
    const element2 = 20;
    const element3 = 4;
    expect(solution(element1, element2, element3)).toEqual(10);
    done();
  });

});
