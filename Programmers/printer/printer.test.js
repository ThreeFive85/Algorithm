import printer from './printer';

describe('printer TEST', () => {
  test('return type number of printer())', (done) => {
    expect(typeof printer([2, 1, 3, 2], 2)).toEqual('number');
    done();
  });

  test('should be return 1 of printer([2, 1, 3, 2], 2)', (done) => {
    expect(printer([2, 1, 3, 2], 2)).toEqual(1);
    done();
  });

  test('should be return 5 of printer([1, 1, 9, 1, 1, 1], 0)', (done) => {
    expect(printer([1, 1, 9, 1, 1, 1], 0)).toEqual(5);
    done();
  });
});
