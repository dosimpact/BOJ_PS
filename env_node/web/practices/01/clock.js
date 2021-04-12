const clockEl = document.querySelector("#clock");

function updateTime() {
  const date = new Date();
  const time = `${date.getHours()} : ${date.getMinutes()} : ${date.getSeconds()}`;
  clockEl.innerHTML = `<span>${time}</span>`;
}

function clockInit() {
  updateTime();
  setInterval(updateTime, 1000);
}

clockInit();
