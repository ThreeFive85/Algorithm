import { solution } from './cacheCities.js';

describe('cacheCities TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = 5;
    const element2 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                        "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"];
    expect(typeof solution(element1, element2)).toEqual('number');
    done();
  });

  test('should return 52', (done) => {
    const element1 = 5;
    const element2 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                        "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"];
    expect(solution(element1, element2)).toEqual(52);
    done();
  });

  test('should return 16', (done) => {
    const element1 = 2;
    const element2 = ["Jeju", "Pangyo", "NewYork", "newyork"];
    expect(solution(element1, element2)).toEqual(16);
    done();
  });

  test('should return 25', (done) => {
    const element1 = 0;
    const element2 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"];
    expect(solution(element1, element2)).toEqual(25);
    done();
  });
});