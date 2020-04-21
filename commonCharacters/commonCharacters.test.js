import commonCharacters from './commonCharacters';

describe('commonCharacters TEST', () => {
  test('should return common characters for simple strings', (done) => {
    expect(commonCharacters('abc', 'abc')).toEqual('abc');
    expect(commonCharacters('ab', 'bc')).toEqual('b');
    done();
  });

  test('should return the common characters in the order they appear', (done) => {
    expect(commonCharacters('zyx', 'xzy')).toEqual('zyx');
    done();
  });

  test('should return the original string for repeated versions of a characters', (done) => {
    const result = commonCharacters('aeiou', 'aaeeiioouu');
    expect(result).toEqual(result, 'aeiou');
    done();
  });

  test('should return the common characters for this anagram', (done) => {
    const string1 = 'all boys love fudge';
    const string2 = 'boys all love fudge';
    const result = commonCharacters(string1, string2);
    expect(result).toEqual(result, 'alboysvefudg');
    done();
  });

  test('should return "" if the first string is ""', (done) => {
    expect(commonCharacters('', '')).toEqual('');
    done();
  });

  test('Extra Credit: should return common characters between more than two strings', (done) => {
    const result = commonCharacters(
      'qwerty',
      'wertyu',
      'ertyui',
      'rtyui',
      'tyuiop',
      'yuiopa',
    );
    expect(result).toEqual('y');
    done();
  });
});
