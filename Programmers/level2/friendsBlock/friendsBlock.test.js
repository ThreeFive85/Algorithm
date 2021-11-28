import { solution } from './friendsBlock.js';

describe('friendsBlock TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 4;
    const element2 = 5;
    const element3 = ["CCBDE", "AAADE", "AAABF", "CCBBF"];
    expect(typeof solution(element1, element2, element3)).toEqual('number');
    done();
  });

  test('should return 14', (done) => {
    const element1 = 4;
    const element2 = 5;
    const element3 = ["CCBDE", "AAADE", "AAABF", "CCBBF"];
    expect(solution(element1, element2, element3)).toEqual(14);
    done();
  });

  test('should return 15', (done) => {
    const element1 = 6;
    const element2 = 6;
    const element3 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"];
    expect(solution(element1, element2, element3)).toEqual(15);
    done();
  });

});