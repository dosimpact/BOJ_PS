function solution(type, id, listener) {
  const children = [];
  const parent = null;
  return {
    type,
    id,
    onEvent(event) {
      for (let p of children) {
        if (p) {
          p.onEvent(event);
        }
      }
      listener(event);
    },
    addChild(node) {
      children.push(node);
    },
    removeChild(node) {
      children.splice(children.indexOf(node), 1);
    },
    children,
  };
}
// <div id="root" /> 를 생성
const rootElement = solution("div", "root", (e) => console.log(`root: ${e}`));

const firstElement = solution("div", "first", (e) =>
  console.log(`first: ${e}`)
);
const secondElement = solution("div", "second", (e) =>
  console.log(`second: ${e}`)
);

rootElement.addChild(firstElement);
rootElement.addChild(secondElement);

const firstInputElement = solution("div", "first-input", (e) =>
  console.log(`first-input: ${e}`)
);
const secondInputElement = solution("div", "second-input", (e) =>
  console.log(`second-input: ${e}`)
);
firstElement.addChild(firstInputElement);
secondElement.addChild(secondInputElement);

firstInputElement.onEvent("click event");
console.log(firstInputElement.children);
