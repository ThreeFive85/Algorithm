import { solution } from './camouflage.js';

describe('camouflage TEST', () => {
  test('should return type of result "number"', (done) => {
    const element1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]];
    expect(typeof solution(element1)).toEqual('number');
    done();
  });

  test('should return 5', (done) => {
    const element1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]];
    expect(solution(element1)).toEqual(5);
    done();
  });

  test('should return 3', (done) => {
    const element1 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]];
    expect(solution(element1)).toEqual(3);
    done();
  });

});