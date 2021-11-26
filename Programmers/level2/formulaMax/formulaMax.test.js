import { solution } from './formulaMax.js';

describe('formulaMax TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = "100-200*300-500+20";
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 60420', (done) => {
    const element1 = "100-200*300-500+20";
    expect(solution(element1)).toEqual(60420);
    done();
  });

  test('should return 300', (done) => {
    const element1 = "50*6-3*2";
    expect(solution(element1)).toEqual(300);
    done();
  });

});