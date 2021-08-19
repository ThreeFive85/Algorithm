import { solution } from './checkScores.js';

describe('checkScores TEST', () => {
  test('should return type of result "string"', (done) => {
    const element1 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
    expect(typeof solution(element1)).toEqual('string');
    done();
  });

  test('should return "FBABD"', (done) => {
    const element1 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
    expect(solution(element1)).toEqual('FBABD');
    done();
  });

  test('should return "DA"', (done) => {
    const element1 = [[50,90],[50,87]]
    expect(solution(element1)).toEqual('DA');
    done();
  });

  test('should return "CFD"', (done) => {
    const element1 = [[70,49,90],[68,50,38],[73,31,100]]
    expect(solution(element1)).toEqual('CFD');
    done();
  });
});
