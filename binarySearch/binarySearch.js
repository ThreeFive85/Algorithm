/*
 * Given a sorted array, find the index of an element
 * using a binary search algorithm.
 *
 * Example usage:
 *
 * var index = binarySearch([1, 2, 3, 4, 5], 4);
 * console.log(index); // [3]
 */

const binarySearch = (arr, target) => {
  let count = 0;

  if (!arr.includes(target)) {
    return null;
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== target) {
      count++;
    } else {
      return count;
    }
  }
};

export default binarySearch;
