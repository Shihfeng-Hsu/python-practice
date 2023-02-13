// A demo of javascript promise
const productAfterDelay = (result, delay) => {
  return new Promise((resolve, reject) => {
    const callback = () => {
      console.log(result);
      resolve(result);
    };
    setTimeout(callback, delay);
  });
};

const promisesArr = [
  productAfterDelay("1", 3000),
  productAfterDelay("2", 1000),
  productAfterDelay("3", 7000),
  productAfterDelay("4", 5000),
  productAfterDelay("5", 6000),
  productAfterDelay("6", 2000),
];
Promise.all(promisesArr); //2 6 1 4 5 3

Promise.any(promisesArr).then((result) => {
  console.log(`The fastest is ${result}`);
}); // 2 The fastest is 2 6 1 4 5

Promise.race(promisesArr);
