const combination = (array, n) => {
  if (array.length < n) {
    return [];
  }
  if (n === 1) {
    // 1以外の場合と形をあわせる
    return array.map((a) => [a]);
  }

  const result = [];

  for (let i = 0; i < array.length; i++) {
    let row = combination(array.slice(i + 1), n - 1);
    for (let j = 0; j < row.length; j++) {
      result.push([array[i]].concat(row[j]));
    }
  }
  return result;
};
// @params range [['会心', 0.2, 0.16], ['痛恨', 0.3, 0.24]...]
function toCombinationPercent(rangeWithEmpty) {
  // 空も含めて送られてくるので空捨てる
  const range = rangeWithEmpty.filter((arr) => arr[0] && arr[1] && arr[2]);
  // { '会心': [0.2, 0.16], '痛恨': [0.3, 0.24]...}
  const abilities = range.reduce((acc, val) => {
    const [name, value, rate] = val;
    acc[name] = [value, rate];
    return acc;
  }, {});
  // ['会心', '痛恨', '心眼'...]
  const abilityNames = Object.keys(abilities);

  const combinations = [...Array(abilityNames.length)]
    .map((_, i) => i + 1)
    .flatMap((n) => {
      return combination(abilityNames, n);
    });
  const result = [...combinations, ["無発動"]].map((arr) => {
    let totalValue = 0;
    // 該当組み合わせの発生率
    const totalRate = abilityNames
      .map((name) => {
        const [value, rate] = abilities[name];
        if (arr.includes(name)) {
          totalValue += value;
          return rate;
        } else {
          // 発動しない確率を返す
          return 1 - rate;
        }
      })
      .reduce((acc, val) => acc * val, 1);
    return [arr.join("+"), totalValue, Math.floor(totalRate * 1000) / 1000];
  });
  console.log(result);
}

toCombinationPercent([
  ["会心", 0.2, 0.16],
  ["痛恨", 0.3, 0.24],
]);
