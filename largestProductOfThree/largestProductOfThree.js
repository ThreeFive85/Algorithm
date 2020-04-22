/**
 *
 * Implement a `DFSelect` method on this Tree class.
 *
 * DFSelect accepts a filter function, calls that function on each of the nodes
 * in Depth First order, and returns a flat array of node values of the tree
 * for which the filter returns true.
 *
 * Example:
 *   var root1 = new Tree(1);
 *   var branch2 = root1.addChild(2);
 *   var branch3 = root1.addChild(3);
 *   var leaf4 = branch2.addChild(4);
 *   var leaf5 = branch2.addChild(5);
 *   var leaf6 = branch3.addChild(6);
 *   var leaf7 = branch3.addChild(7);
 *   root1.DFSelect(function (value, depth) {
 *     return value % 2;
 *   })
 *   // [1, 5, 3, 7]
 *
 *   root1.DFSelect(function (value, depth) {
 *     return depth === 1;
 *   })
 *   // [2, 3]
 *
 */

/*
 * Basic tree that stores a value.
 */

const largestProductOfThree = (array) => {
  return array
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((acc, cur) => acc * cur);
};

export default largestProductOfThree;
