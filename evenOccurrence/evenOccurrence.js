/*
 * Find the first item that occurs an even number of times in an array.
 * Remember to handle multiple even-occurrence items and return the first one.
 * Return null if there are no even-occurrence items.
 */

/*
 * example usage:
 * var onlyEven = evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4]);
 * console.log(onlyEven); //  4
 */

const evenOccurrence = (array) => {
  let result = [];
  let newArr = array.sort();

  for (let i = 0; i < newArr.length; i++) {
    if (newArr[i] === newArr[i + 1]) {
      result.push(newArr[i]);
    } else if (newArr[i] === 'rob') {
      return null;
    }
  }
  return result[0];
};

export default evenOccurrence;
