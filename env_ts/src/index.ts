const WEEKES = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
const MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30];

function solution(a: number, b: number) {
  let days = 0;

  // 2 > 31 , 3 > 31,29
  for (let i = 0; i < a - 1; i++) {
    days += MONTHS[i];
  }
  days += b;

  return WEEKES[Math.floor((days + 4) % 7)];
}

solution(5, 24);
