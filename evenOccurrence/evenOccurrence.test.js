import evenOccurrence from './evenOccurrence';

describe('evenOccurrence TEST', () => {
  test('should return the first even occurrence of an array of numbers', (done) => {
    expect(evenOccurrence([1, 3, 3, 3, 2, 4, 4, 2, 5])).toEqual(2);
    done();
  });

  test('should return the first even occurrence of an array with strings', (done) => {
    expect(evenOccurrence(['cat', 'dog', 'dig', 'cat'])).toEqual('cat');
    done();
  });

  test('should return the first even occurrence of a mixed array', (done) => {
    expect(evenOccurrence(['meow', 2, 1, 'meow'])).toEqual('meow');
    done();
  });

  test('should return the first even occurrence in an array with multiple even occurrences', (done) => {
    const array = ['doublerainbow', 'grumpycat', 'grumpycat', 'doublerainbow'];
    expect(evenOccurrence(array)).toEqual('doublerainbow');
    done();
  });

  test('should return `null` when no items occur an even number of times', (done) => {
    const array = ['rob', 'victor', 'fred', 'jess', 'rob', 'rob'];
    expect(evenOccurrence(array)).toEqual(null);
    done();
  });
});
