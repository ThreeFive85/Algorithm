/**
 * Write a function that, given two objects, returns whether or not the two
 * are deeply equivalent--meaning the structure of the two objects is the
 * same, and so is the structure of each of their corresponding descendants.
 *
 * Examples:
 *
 * deepEquals({a:1, b: {c:3}},{a:1, b: {c:3}}); // true
 * deepEquals({a:1, b: {c:5}},{a:1, b: {c:6}}); // false
 *
 * don't worry about handling cyclical object structures.
 *
 */

const deepEquals = (apple, orange) => {
  let result = false;

  // let appleKey = Object.keys(apple).sort();
  // let orangeKey = Object.keys(orange).sort();
  // //   console.log(appleKey);
  //   console.log(JSON.stringify(apple));
  if (JSON.stringify(apple) === JSON.stringify(orange)) {
    return true;
  }
  for (let k in apple) {
    if (typeof apple[k] === 'object' && typeof orange[k] === 'object') {
      result = deepEquals(apple[k], orange[k]);
    }
  }
  return result;
};

export default deepEquals;
