// make a  little progressor

// xx.xx% downloaded ( ..MB of oo MB )

const readline = require("readline");

const progressor = (downloaded, total) => {
  const percentage = ((downloaded / total) * 100).toFixed(2);
  readline.cursorTo(process.stdout, 0);
  process.stdout.write(
    `${percentage} is downloaded..( ${(downloaded / 1024 / 1024).toFixed(
      2
    )}MB  of ${(total / 1024 / 1024).toFixed(2)}MB) ${
      downloaded >= total - 2000 ? "✔\n" : ""
    }`
  );
};

const downloader = async () => {
  for (let i = 0; i < 31000000; i += 1900) {
    progressor(i, 31000000);
  }
};
const main = () => {
  downloader();
  downloader();
};
main();

const ins = `
var i = 0;\n
while(i < 10){\n
  console.log(i)\n
  i++ \n
`;
