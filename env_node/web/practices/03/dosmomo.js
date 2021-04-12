// fetcher

const problemListEl = document.querySelector("#problemList");
const problemFormEl = document.querySelector("#problemForm");
const problemSubmitBtnEl = document.querySelector("#problemSubmitBtn");

let error = null;
let loading = false;
let data = null;
let answerSheet = {};

async function fetchProblems() {
  loading = true;
  try {
    const response = await fetch("https://dosmomo.herokuapp.com/problems01/");
    data = await response.json();
    console.log(data);
    if (!data?.ok) {
      throw new Error("cannot fetch Data");
    }
  } catch (error) {
    console.error("cannot fetch Data");
    error = "cannot fetch Data";
  }
  loading = false;
}
async function fetchCheckProblem() {
  try {
    const response = await fetch(
      "https://dosmomo.herokuapp.com/problems01/check",
      {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: 18,
          answer: ["1", "3", "4"],
        }),
      }
    );
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

// event handler
function handleSubmit(e) {
  e.preventDefault();
  _handleSubmit_parseAnsSheet();
  _handleSubmit_checkData();
}
function _handleSubmit_parseAnsSheet() {
  const ids = [];
  let ansNodeEl = [];
  for (const problem of data?.problems01 || []) {
    ids.push(problem.id);
  }
  if (ids) {
    ids.map((id) => {
      const res = document.querySelectorAll(`#p-${id}`);
      ansNodeEl.push(...res);
    });
  }
  ansNodeEl = ansNodeEl.filter((node) => node.checked === true);
  answerSheet = {};
  ansNodeEl.forEach((node) => {
    const id = Number(node.getAttribute("id").substring(2));
    const answer = node.value;
    if (id in answerSheet) {
      answerSheet[id].push(answer);
    } else {
      answerSheet[id] = [answer];
    }
  });
  //   console.log(answerSheet);
}

function _handleSubmit_checkData() {
  console.log(answerSheet);
}

// render
async function problemRender(problem) {
  console.log(problem);
  const isNumber = problem?.answer?.isNumber;

  const itemEl = document.createElement("li");
  const titleEl = document.createElement("h5");
  const subTitleEl = document.createElement("h6");

  titleEl.innerHTML = problem?.title;
  subTitleEl.innerHTML = problem?.subTitle;
  itemEl.appendChild(titleEl);
  itemEl.appendChild(subTitleEl);

  if (isNumber) {
    //객관식 랜더링
    Array.from(Array(4).keys(), (_, i) => i + 1).map((n) => {
      const labelEl = document.createElement("label");
      labelEl.innerHTML = `${n}번`;
      const inputEl = document.createElement("input");
      inputEl.type = "checkbox";
      inputEl.setAttribute("id", `p-${problem?.id}`);
      inputEl.name = `p-${n}`;
      inputEl.value = n;
      itemEl.appendChild(labelEl);
      itemEl.appendChild(inputEl);
    });
  } else {
    // 주관식 랜더링
    const inputEl = document.createElement("input");
    inputEl.type = "text";
    inputEl.placeholder = "주관식 정답 입력";
    inputEl.setAttribute("id", `p-${problem?.id}`);
    inputEl.setAttribute("checked", true);
    itemEl.appendChild(inputEl);
  }

  problemListEl.appendChild(itemEl);
}
async function problemsRender() {
  if (!error && data?.problems01) {
    await Promise.all(
      data?.problems01.map(async (problem) => {
        problemRender(problem);
      })
    );
  }
}
async function resultRender() {}

async function dosmomoInit() {
  console.log("dosmomoInit");
  problemFormEl.addEventListener("submit", handleSubmit);
  await fetchProblems();
  await problemsRender();
  await fetchCheckProblem();
}
dosmomoInit();
