import { solution } from './countString.js';

describe('countString TEST', () => {
    test('should return type of result "boolean"', (done) => {
      expect(typeof solution("pPoooyY")).toEqual('boolean');
      done();
    });
  
    test('should return false', (done) => {
      expect(solution("pyyy")).toEqual(false);
      done();
    });
  
    test('should return true', (done) => {
      expect(solution("pPoooyY")).toEqual(true);
      done();
    });

    test('should return false', (done) => {
        expect(solution("PPoiouY")).toEqual(false);
        done();
      });
  });