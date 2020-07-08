import passingAbridge from './passingAbridge';

describe('passingAbride TEST', () => {
  test('should be type return number of passingAbridge()', (done) => {
    const resultType = passingAbridge(2, 10, [7, 4, 5, 6]);
    expect(typeof resultType).toEqual('number');
    done();
  });

  test('should be return 8 of passingAbridge(2,10,[7,4,5,6])', (done) => {
    const result = passingAbridge(2, 10, [7, 4, 5, 6]);
    expect(result).toEqual(8);
    done();
  });
});
