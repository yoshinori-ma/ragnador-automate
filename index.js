const { default: gf } = require("good-friends-colors");

const r1 = process.argv[2];
const g1 = process.argv[3];
const b1 = process.argv[4];

const r2 = process.argv[5];
const g2 = process.argv[6];
const b2 = process.argv[7];

const result = gf({ r: r1, g: g1, b: b1 }).diff({
  r: r2,
  g: g2,
  b: b2,
});

process.stdout.write(result.toString());
