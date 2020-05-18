import characterFrequency from './characterFrequency';

describe('characterFrequency TEST', () => {
  test('should return an array of arrays', (done) => {
    const result = characterFrequency('good');
    expect(result).toEqual(expect.arrayContaining(result));
    done();
  });

  test('should return key-value pairs of letters and numbers', (done) => {
    const result = characterFrequency('good');
    expect(typeof result[0][0]).toEqual('string');
    expect(typeof result[0][1]).toEqual('number');
    done();
  });

  test('should return one key-value pair for each unique letter in the string', (done) => {
    const result = characterFrequency('aabbc');
    expect(result.length).toEqual(3);
    done();
  });

  test('should sort by descending order in frequency', (done) => {
    const result = characterFrequency('mississippi');
    expect(result[0][1]).toEqual(4);
    expect(result[1][1]).toEqual(4);
    expect(result[2][1]).toEqual(2);
    expect(result[3][1]).toEqual(1);
    done();
  });

  test('should sort by ascending order of letters', (done) => {
    const result = characterFrequency('yzbzy');
    expect(result[0][0]).toEqual('y');
    expect(result[1][0]).toEqual('z');
    expect(result[2][0]).toEqual('b');
    done();
  });

  test('should sort priorities sorting by frequence over sorting by letter', (done) => {
    let result;
    // same number of p's and o's, sort ascending by character
    result = characterFrequency('popopo');
    expect(result[0][0]).toEqual('o');
    expect(result[1][0]).toEqual('p');
    // more p's and than o's, sort by frequency
    result = characterFrequency('popopop');
    expect(result[0][0]).toEqual('p');
    expect(result[1][0]).toEqual('o');
    done();
  });

  test('should handle the empty string degenerate case', (done) => {
    const result = characterFrequency('');
    expect(result).toEqual([]);
    done();
  });

  test('should give the expected result for `supercalifragilisticexpialidocious`', (done) => {
    const input = characterFrequency('supercalifragilisticexpialidocious');
    const output = [
      ['i', 7],
      ['a', 3],
      ['c', 3],
      ['l', 3],
      ['s', 3],
      ['e', 2],
      ['o', 2],
      ['p', 2],
      ['r', 2],
      ['u', 2],
      ['d', 1],
      ['f', 1],
      ['g', 1],
      ['t', 1],
      ['x', 1],
    ];
    expect(input).toEqual(output);
    done();
  });
});
