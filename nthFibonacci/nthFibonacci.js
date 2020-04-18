const nthFibonacci = (n) => {
  let first = 0;
  let second = 1;
  let result = 0;

  if (n === 1) {
    return 1;
  }
  for (let i = 1; i < n; i++) {
    result = first + second;
    first = second;
    second = result;
  }
  return result;
};

export default nthFibonacci;
