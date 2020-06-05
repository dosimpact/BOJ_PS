// make a  little progressor

// xx.xx% downloaded ( ..MB of oo MB )

const readline = require("readline");

const progressor = (downloaded, total) => {};

for (let i = 0; i < 31000000; i += 1000) {
  progressor(i, 31000000);
}
