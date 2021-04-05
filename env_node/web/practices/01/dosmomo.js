const problemsListEl = document.querySelector("#problemsList");
const problemsFormEl = document.querySelector("#problemsForm");
const problemsResultEl = document.querySelector("#problemsResult");

let answerSheet = [];
let problems = [];

async function fetchData() {
  console.log("fetchData");
  const respoense = await fetch("https://dosmomo.herokuapp.com/problems01/");
  const { problems01 } = await respoense.json();
  problems = problems01;
  console.log(problems);
  renderProblems();
}

async function fetchCheckProblem(sheet) {
  const res = await fetch("https://dosmomo.herokuapp.com/problems01/check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: Number(sheet.id),
      answer: sheet.answer, //["1", "2", "3", "4"],
    }),
  });
  const data = await res.json();
  console.log(data);
  return data;
}

// renderer

function renderProblemNumber(p) {
  const problemContainerEl = document.createElement("div");
  const titleEl = document.createElement("div");
  const subTitleEl = document.createElement("div");

  titleEl.innerHTML = `<h5><strong>${p.id}</strong> ${p.title}</h5>`;
  subTitleEl.innerHTML = p.subTitle;
  problemContainerEl.appendChild(titleEl);
  problemContainerEl.appendChild(subTitleEl);
  problemContainerEl.id = `problem_${p.id}`;

  Array.from(Array(4), (_, i) => i + 1).forEach((e) => {
    const labelEl = document.createElement("label");
    const inputEl = document.createElement("input");
    labelEl.innerHTML = e;
    labelEl.for = `id-${p.id}`;
    inputEl.type = "checkbox";
    inputEl.id = `id-${p.id}`;
    inputEl.name = `id-${p.id}`;
    inputEl.value = e;
    problemContainerEl.appendChild(labelEl);
    problemContainerEl.appendChild(inputEl);
  });

  problemsListEl.appendChild(problemContainerEl);
}

function renderProblemText(p) {
  const problemContainerEl = document.createElement("div");
  const titleEl = document.createElement("div");
  const subTitleEl = document.createElement("div");

  titleEl.innerHTML = `<h5><strong>${p.id}</strong> ${p.title}</h5>`;
  subTitleEl.innerHTML = p.subTitle;
  problemContainerEl.appendChild(titleEl);
  problemContainerEl.appendChild(subTitleEl);
  problemContainerEl.id = `problem_${p.id}`;

  const labelEl = document.createElement("label");
  const inputEl = document.createElement("input");
  labelEl.innerHTML = "주관식 : ";
  labelEl.for = `id-${p.id}`;
  inputEl.type = "text";
  inputEl.id = `id-${p.id}`;
  inputEl.name = `id-${p.id}`;
  inputEl.value = "";
  problemContainerEl.appendChild(labelEl);
  problemContainerEl.appendChild(inputEl);

  problemsListEl.appendChild(problemContainerEl);
}

function renderProblems() {
  problems.forEach((p) => {
    if (p.answer.isNumber) {
      renderProblemNumber(p);
    } else {
      renderProblemText(p);
    }
  });
}

function rednerResult() {}
// DOM Search

function _getAnswers() {
  answerSheet = [];
  // 1~100 문제 제한
  Array.from(Array(30), (_, i) => i + 1).forEach((e) => {
    const collections = document.querySelectorAll(`#id-${e}`);
    // 랜더링 된 문제인 경우
    if (collections.length >= 1) {
      // 주관식  //객관식
      if (collections.length == 1) {
        const id = collections[0].id.substring(3);
        const answer = [collections[0].value];
        // console.log("==>", id, answer);
        answerSheet.push({ id, answer });
      } else {
        const id = String(collections[0].name).substring(3);
        const answer = [];
        Array.from(collections).forEach((node) => {
          if (node.checked) {
            answer.push(node.value);
          }
        });
        // console.log("==>", id, answer);
        answerSheet.push({ id, answer });
      }
    }
  });
}

// handler answer

async function _checkProblemsAndRender() {
  const res = await Promise.all(
    answerSheet.map(async (sheet) => {
      return fetchCheckProblem(sheet);
    })
  );
  console.log(res);
  let commentC = "";
  let commentC_cnt = 0;
  let commentW = "";
  let commentW_cnt = 0;
  for (let i = 0; i < answerSheet.length; i++) {
    if (res[i].isCorrect) {
      commentC += `${answerSheet[i].id},`;
      commentC_cnt += 1;
    } else {
      commentW += `${answerSheet[i].id},`;
      commentW_cnt += 1;
    }
  }
  problemsResultEl.innerHTML = `${commentC}(${commentC_cnt})/${commentW}(${commentW_cnt})`;
}

function handleCheckProblem(e) {
  e.preventDefault();
  console.log("handleCheckProblem");
  _getAnswers();
  console.log(answerSheet);
  _checkProblemsAndRender();
}

// init
function dosmomoInit() {
  fetchData();
  problemsFormEl.addEventListener("submit", handleCheckProblem);
}
dosmomoInit();
