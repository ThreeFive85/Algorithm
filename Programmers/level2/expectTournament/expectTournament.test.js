import { solution } from './expectTournament.js';

describe('expectTournament TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 8;
    const element2 = 4;
    const element3 = 7;
    expect(typeof solution(element1, element2, element3)).toEqual('number');
    done();
  });

  test('should return 3', (done) => {
    const element1 = 8;
    const element2 = 4;
    const element3 = 7;
    expect(solution(element1, element2, element3)).toEqual(3);
    done();
  });

});