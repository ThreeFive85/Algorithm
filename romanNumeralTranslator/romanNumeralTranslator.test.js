import translateRomanNumeral from './romanNumeralTranslator';

describe('romanNumeralTranslator TEST', () => {
  test('should translate I', (done) => {
    expect(translateRomanNumeral('I')).toEqual(1);
    done();
  });

  test('should translate V', (done) => {
    expect(translateRomanNumeral('V')).toEqual(5);
    done();
  });

  test('should translate X', (done) => {
    expect(translateRomanNumeral('X')).toEqual(10);
    done();
  });

  test('should translate L', (done) => {
    expect(translateRomanNumeral('L')).toEqual(50);
    done();
  });

  test('should translate C', (done) => {
    expect(translateRomanNumeral('C')).toEqual(100);
    done();
  });

  test('should translate D', (done) => {
    expect(translateRomanNumeral('D')).toEqual(500);
    done();
  });

  test('should translate M', (done) => {
    expect(translateRomanNumeral('M')).toEqual(1000);
    done();
  });

  test('should translate multiple digits being added', (done) => {
    expect(translateRomanNumeral('II')).toEqual(2);
    expect(translateRomanNumeral('VI')).toEqual(6);
    expect(translateRomanNumeral('VII')).toEqual(7);
    expect(translateRomanNumeral('XV')).toEqual(15);
    done();
  });

  test('should translate subtractive notation', (done) => {
    expect(translateRomanNumeral('IV')).toEqual(4);
    expect(translateRomanNumeral('XIV')).toEqual(14);
    expect(translateRomanNumeral('MCM')).toEqual(1900);
    done();
  });

  test('should translate complex examples (e.g. years used in Wikipedia page on roman numerals)', (done) => {
    expect(translateRomanNumeral('MCMLIV')).toEqual(1954);
    expect(translateRomanNumeral('MCMXC')).toEqual(1990);
    expect(translateRomanNumeral('MMVIII')).toEqual(2008);
    expect(translateRomanNumeral('MDCCCCX')).toEqual(1910);
    expect(translateRomanNumeral('MCMX')).toEqual(1910);
    done();
  });

  test('should return null if passed something other than a string', (done) => {
    expect(translateRomanNumeral(50)).toEqual(null);
    done();
  });

  test('should return 0 if passed an empty string', (done) => {
    expect(translateRomanNumeral('')).toEqual(0);
    done();
  });
});
