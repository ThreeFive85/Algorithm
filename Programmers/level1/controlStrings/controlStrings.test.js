import { solution } from './controlStrings.js';

describe('controlStrings TEST', () => {
    test('should return type of result "boolean"', (done) => {
      expect(typeof solution("a234")).toEqual('boolean');
      done();
    });
  
    test('should return false', (done) => {
      expect(solution("a234")).toEqual(false);
      done();
    });
  
    test('should return true', (done) => {
      expect(solution("1234")).toEqual(true);
      done();
    });

    test('should return false', (done) => {
        expect(solution("1e22")).toEqual(false);
        done();
      });
  });