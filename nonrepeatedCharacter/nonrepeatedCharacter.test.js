import firstNonRepeatedCharacter from './nonrepeatedCharacter';

describe('Test', () => {
  test('should return the first nonrepeated character in the string `ABA`', (done) => {
    expect(firstNonRepeatedCharacter('ABA')).toEqual('B');
    done();
  });

  test('should return `null` for strings that have every character repeated', (done) => {
    expect(firstNonRepeatedCharacter('XXXXX')).toEqual(null);
    done();
  });

  test('should return the first nonrepeating character in the string `AABCABD`', (done) => {
    expect(firstNonRepeatedCharacter('AABCABD')).toEqual('C');
    done();
  });
});
