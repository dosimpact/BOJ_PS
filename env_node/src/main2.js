/*
 * 현재 온라인인 보험 전문가의 목록을 반환하도록 함수를 작성해주세요.
 * (반환 타입: Promise<string[]>)
 */
async function solution(fetchExperts, fetchIsExpertOnline) {
  // 보험 전문가의 목록을 반환하는 비동기 함수 (반환 타입: Promise<string[]>)
  const data = await fetchExperts();
  const res = await Promise.all(data.map((d) => fetchIsExpertOnline(d)));
  console.log(res);
  return data.filter((d, i) => res[i]);
  // 보험 전문가가 온라인인지 여부를 반환하는 함수 (반환 타입: Promise<boolean>)
  // fetchIsExpertOnline('배수진');
}
