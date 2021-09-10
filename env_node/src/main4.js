// async function solution(callAPI) {
//   const token = null;

//   return new Promise(async (resolve) => {
//     if (token) {
//       const res = await callAPI(token);
//       this.token = res.token;
//       resolve(res.result);
//     } else {
//       const res = await callAPI();
//       this.token = res.token;
//       resolve(res.result);
//     }
//   });
// }
// async function solution(callAPI) {
//   const token = null;
//   return async () => {
//     if (token) {
//       const res = await callAPI(token);
//       this.token = res.token;
//       return res.result;
//     } else {
//       const res = await callAPI();
//       this.token = res.token;
//       return res.result;
//     }
//   };
// }
async function solution(callAPI) {
  const token = null;
  return async () => {
    if (token) {
      const res = await callAPI(token);
      this.token = res.token;
      return res.result;
    } else {
      const res = await callAPI();
      this.token = res.token;
      return res.result;
    }
  };
}
