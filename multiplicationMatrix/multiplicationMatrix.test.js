import multiplicationMatrix from './multiplicationMatrix';

describe('multiplicationMatrix TEST', () => {
  test('test', (done) => {
    const matrix1 = [
      [4, -1],
      [2, 3],
      [1, 5],
    ];
    const matrix2 = [
      [7, -3],
      [9, -2],
    ];
    expect(multiplicationMatrix(matrix1, matrix2)).toEqual([
      [19, -10],
      [41, -12],
      [52, -13],
    ]);
    done();
  });
});
