/**
 *  A = [4,-1]
 *      [2, 3]
 *      [1, 5]
 *
 *  B = [7,-3]
 *      [9,-2]
 */

const multiplicationMatrix = (matrix1, matrix2) => {
  let result = [];

  for (let i = 0; i < matrix1.length; i++) {
    result.push([]);
    for (let j = 0; j < matrix2[0].length; j++) {
      result[i].push(0);
    }
  }

  for (let i = 0; i < matrix1.length; i++) {
    for (let j = 0; j < matrix2[0].length; j++) {
      for (let k = 0; k < matrix1[0].length; k++) {
        result[i][j] += matrix1[i][k] * matrix2[k][j];
      }
    }
  }
  return result;
};

export default multiplicationMatrix;

/**
 * var answer = [];
  var row1 = arr1.length;
  var col1 = arr1[0].length;
  var col2 = arr2[0].length;

  for (var s = 0; s < row1; s++) {
    answer.push([]);
    for (var x = 0; x < col2; x++) {
      answer[s].push(0);
    }
  }

  for (var i = 0; i < row1; i++) {
    for (var j = 0; j < col2; j++) {
      for (var k = 0; k < col1; k++) {
        answer[i][j] = answer[i][j] + arr1[i][k] * arr2[k][j];
      }
    }
  }

  return answer;
 */

/**
  *  return Array(arr1.length).fill()
      .map((r, i) => Array(arr2[0].length).fill()
           .map((v, j) => arr1[i].reduce((a, c, k) => a + c * arr2[k][j], 0)))
  */
