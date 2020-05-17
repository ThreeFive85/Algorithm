// import primeTester from './primeTest';
// import primeSieve from './primeTest';

const primeTester = require('./primeTest').primeTester;
const primeSieve = require('./primeTest').primeSieve;

describe('primeTester, primeSieve TEST', () => {
  describe('primeTest TEST', () => {
    test('should return a boolean', (done) => {
      expect(typeof primeTester(3)).toEqual('boolean');
      done();
    });

    test('should return `true` for the prime number 2', (done) => {
      expect(primeTester(2)).toEqual(true);
      done();
    });

    test('should return `false` for the non-prime number 1', (done) => {
      expect(primeTester(1)).toEqual(false);
      done();
    });

    test('should return `true` for the prime number 15485867', (done) => {
      expect(primeTester(15485867)).toEqual(true);
      done();
    });

    test('should return `false` for the non-prime `15485867 * 15485867`', (done) => {
      expect(primeTester(15485867 * 15485867)).toEqual(false);
      done();
    });

    test('should return `true` for the prime number `2971215073`', (done) => {
      expect(primeTester(2971215073)).toEqual(true);
      done();
    });

    test('should return `false` for the non-prime `2971215073 * 2971215073`', (done) => {
      expect(primeTester(2971215073 * 2971215073)).toEqual(false);
      done();
    });

    test('should return `true` for the prime number `70368760954879`', (done) => {
      expect(primeTester(70368760954879)).toEqual(true);
      done();
    });

    test('should return `false` for the non-prime `70368760954879 - 1`', (done) => {
      expect(primeTester(70368760954879 - 1)).toEqual(false);
      done();
    });
  });
  describe('primeSieve TEST', () => {
    test('should return an empty array between 20 and 22 (no primes)', (done) => {
      expect(primeSieve(20, 22)).toEqual([]);
      done();
    });

    test('should return every prime between 1 and 2', (done) => {
      expect(primeSieve(1, 2)).toEqual([2]);
      done();
    });

    test('should return every prime between 1 and 2', (done) => {
      expect(primeSieve(2, 2)).toEqual([2]);
      done();
    });

    test('should return every prime between 1 and 10', (done) => {
      expect(primeSieve(1, 10)).toEqual([2, 3, 5, 7]);
      done();
    });

    test('should return the primes between 23 and 29 (inclusive)', (done) => {
      expect(primeSieve(23, 29)).toEqual([23, 29]);
      done();
    });

    test('should return every prime between 2908 and 3080', (done) => {
      expect(primeSieve(2908, 3080)).toEqual([
        2909,
        2917,
        2927,
        2939,
        2953,
        2957,
        2963,
        2969,
        2971,
        2999,
        3001,
        3011,
        3019,
        3023,
        3037,
        3041,
        3049,
        3061,
        3067,
        3079,
      ]);
      done();
    });
  });
});
