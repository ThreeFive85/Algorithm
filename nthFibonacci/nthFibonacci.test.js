import nthFibonacci from './nthFibonacci';

describe('nthFibonacci', () => {
  test('should return integers', (done) => {
    const result = nthFibonacci(0);
    expect(typeof result).toBe('number');
    done();
  });

  test('should handle the base cases with ease', (done) => {
    expect(nthFibonacci(0)).toEqual(0);
    expect(nthFibonacci(1)).toEqual(1);
    done();
  });

  test('should return the nth Fibonacci number for a given n', (done) => {
    expect(nthFibonacci(5)).toEqual(5);
    expect(nthFibonacci(10)).toEqual(55);
    expect(nthFibonacci(20)).toEqual(6765);
    done();
  });
  // test('test1', (done) => {
  //   expect(nthFibonacci).toThrow(/nthFibonacci/);
  //   done();
  // });
});
