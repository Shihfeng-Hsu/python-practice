function sumStrings(a, b) {
  let arrA, arrB;
  if (a.length >= b.length) {
    arrA = [...a].reverse();
    arrB = [...b].reverse();
  } else {
    arrA = [...b].reverse();
    arrB = [...a].reverse();
  }

  const doSum = (c, n) => {
    let [x, y] = n;
    c = c || "0";
    console.log(c);
    return String(parseInt(x) + parseInt(y) + parseInt(c)).padStart(2, "0");
  };
  let zip = arrA.map(function (e, i) {
    return [e, arrB[i] || "0"];
  });
  let result = zip.reduce(
    function (acc, n) {
      let appo = doSum(acc[0], n).split("");
      return [appo[0], appo[1] + acc[1]];
    },
    ["0", ""]
  );
  console.log(result);
  return result.join("").replace(/^(0+)/, "");
}

sumStrings("712569312664357328695151392", "8100824045303269669937");
