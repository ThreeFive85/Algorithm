import { solution } from './sortString.js';

describe('sortString TEST', () => {
  test('should return type of result "object"', (done) => {
    const element1 = ["sun", "bed", "car"]
    const element2 = 1
    expect(typeof solution(element1, element2)).toEqual('object');
    done();
  });

  test('should return ["car", "bed", "sun"]', (done) => {
    const element1 = ["sun", "bed", "car"]
    const element2 = 1
    expect(solution(element1, element2)).toEqual(["car", "bed", "sun"]);
    done();
  });

  test('should return ["abcd", "abce", "cdx"]', (done) => {
    const element1 = ["abce", "abcd", "cdx"]
    const element2 = 2
    expect(solution(element1, element2)).toEqual(["abcd", "abce", "cdx"]);
    done();
  });
  
});
