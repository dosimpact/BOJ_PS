const todoFormEl = document.querySelector("#todoForm");
const todoInputEl = document.querySelector("#todoInput");
const todoListEl = document.querySelector("#todoList");

// data C,D
let TodoData = [];

function addTodoData(id, content) {
  TodoData.push({
    id,
    content,
    date: Date.now(),
  });
  console.log(TodoData);
}
function delTodoData(id) {
  const TodoDataFiltered = TodoData.filter((todo) => todo.id !== id);
  TodoData = TodoDataFiltered;
}

// render handler

function _addTodoElement(id, todoContent) {
  const liEl = document.createElement("li");
  const spanContentEl = document.createElement("span");
  const spanDelBtnEl = document.createElement("span");
  //
  spanContentEl.innerHTML = todoContent;
  spanDelBtnEl.innerHTML = " | 💥 삭제";
  spanDelBtnEl.setAttribute("class", "delBtn");
  spanDelBtnEl.style = "cursor:pointer;";
  liEl.appendChild(spanContentEl);
  liEl.appendChild(spanDelBtnEl);
  liEl.setAttribute("id", id);
  todoListEl.appendChild(liEl);
}

function renderTodoElement() {
  todoListEl.innerHTML = "";
  TodoData.map((todo) => {
    _addTodoElement(`todo_${todo.id}`, todo.content);
  });
}

// event handler

function handleSubmit(e) {
  e.preventDefault();
  const todoContent = todoInputEl.value;
  todoInputEl.value = "";
  addTodoData(TodoData.length, todoContent);
  renderTodoElement();
}

function handleDelEvent(e) {
  const className = e.target.getAttribute("class");
  if (className.startsWith("delBtn")) {
    const parentLiEl = e.target.parentNode;
    const id = Number(parentLiEl.getAttribute("id").substr(5));
    console.log("delete", id);
    delTodoData(id);
    renderTodoElement();
  }
}

function todoInit() {
  // console.log("todoInit");
  todoFormEl.addEventListener("submit", handleSubmit);
  todoListEl.addEventListener("click", handleDelEvent);
}

todoInit();
