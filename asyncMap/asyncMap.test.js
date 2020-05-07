import asyncMap from './asyncMap';

describe('asyncMap TEST', () => {
  test('should pass the completed tasks to its callback', (done) => {
    function wait2For2(callback) {
      setTimeout(function () {
        callback(2);
      }, 200);
    }

    function wait3For1(callback) {
      setTimeout(function () {
        callback(1);
      }, 300);
    }

    var res;
    asyncMap([wait2For2, wait3For1], function (arr) {
      res = arr;
      /* This should work regardless of order because of
       * the time it takes to execute these 2 functions
       */
      // res.should.deepEqual([2,1]);
      // res.length.should.equal(2);
      expect(res).toEqual([2, 1]);
      done();
    });
  });

  test('should pass the completed tasks to its callback in the correct order', (done) => {
    function wait2For2(callback) {
      setTimeout(function () {
        callback(2);
      }, 200);
    }

    function wait3For1(callback) {
      setTimeout(function () {
        callback(1);
      }, 300);
    }

    var res;
    asyncMap([wait3For1, wait2For2], function (arr) {
      res = arr;
      expect(res).toEqual([1, 2]);
      done();
    });
  });

  test('should handle more than two async functions in the correct order', (done) => {
    function wait2For2(callback) {
      setTimeout(function () {
        callback(2);
      }, 200);
    }

    function wait5For4(callback) {
      setTimeout(function () {
        callback(4);
      }, 500);
    }

    function wait1For3(callback) {
      setTimeout(function () {
        callback(3);
      }, 100);
    }

    function wait3For1(callback) {
      setTimeout(function () {
        callback(1);
      }, 300);
    }

    function wait1For5(callback) {
      setTimeout(function () {
        callback(5);
      }, 100);
    }

    var res;
    asyncMap([wait3For1, wait2For2, wait1For3, wait5For4, wait1For5], function (
      arr,
    ) {
      res = arr;
      expect(res).toEqual([1, 2, 3, 4, 5]);
      done();
    });
  });
});
