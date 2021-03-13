// ref
const loginFormEl = document.querySelector("#loginForm");
const loginForm_emailEl = document.querySelector("#loginForm_email");
const loginForm_passwordEl = document.querySelector("#loginForm_password");

const tokenOutputEl = document.querySelector("#tokenOutput");
const flagOutputEl = document.querySelector("#flagOutput");
// fetch

async function getUsers() {
  const res = await fetch("https://dosmomo.herokuapp.com/problems02", {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    redirect: "follow",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await res.json();
  console.log(data);
}

async function loginUser(body) {
  const res = await fetch("https://dosmomo.herokuapp.com/problems02/login", {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    redirect: "follow",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  console.log(data);
  if (data.ok) {
    return data.token;
  } else {
    return null;
  }
}

async function checkUser(token) {
  const res = await fetch("https://dosmomo.herokuapp.com/problems02/check", {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    redirect: "follow",
    headers: {
      "Content-Type": "application/json",
      "my-jwt": token,
    },
  });
  const data = await res.json();
  console.log(data);
  if (data.ok) {
    return data.flag;
  } else {
    return null;
  }
}

// handler

async function handle_login(e) {
  e.preventDefault();
  const email = loginForm_emailEl.value;
  const password = loginForm_passwordEl.value;
  console.log(email, password);
  const token = await loginUser({ email, password });
  if (token) {
    renderToken(token);
    const flag = await checkUser(token);
    renderFlag(flag);
  }
}

// render

function renderToken(token) {
  tokenOutputEl.innerHTML = token;
}
function renderFlag(flag) {
  flagOutputEl.innerHTML = flag;
}

// bind Event

function bindEvent() {
  loginFormEl.addEventListener("submit", handle_login);
}

async function problem02() {
  bindEvent();
  console.log("problem02");
  await getUsers();
}

problem02();
