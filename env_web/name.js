const nameFormEl = document.getElementById("nameForm");
const nameInputEl = document.getElementById("nameInput");
const nameDisplayEl = document.getElementById("nameDisplay");

const NAME_KEY_LS = "NAME";

function saveName(name) {
  localStorage.setItem(NAME_KEY_LS, name);
}
function loadName() {
  const localName = localStorage.getItem(NAME_KEY_LS);
  if (localName) {
    nameDisplayEl.innerText = `hello [${localName}]`;
  }
}

function handleSubmitName(e) {
  e.preventDefault();
  console.log(nameInputEl.value);
  const name = nameInputEl.value;
  nameInputEl.value = "";
  nameDisplayEl.innerText = `hello [${name}]`;
  saveName(name);
}

function nameInit() {
  loadName();
  nameFormEl.addEventListener("submit", handleSubmitName);
}

nameInit();
