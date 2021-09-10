const CheckState = {
  checked: "checked",
  unchecked: "unchecked",
  indeterminate: "indeterminate",
};
class CheckItem {
  static from(...args) {
    return new CheckItem(...args);
  }

  constructor(props) {
    /*
     * 아래 3개 멤버는 필수로 존재해야 합니다.
     *  id: string;
     *  state: CheckState;
     *  children: CheckItem[];
     *  parents: CheckItem ? 어떻게 이 정보를 보내지 ?
     */
    this.state = CheckState.unchecked;
    this.id = props.id;
    this.children = [];
    for (let item of props.children) {
      this.children.push(new CheckItem(item));
    }
  }

  toggle() {
    if (this.state === CheckState.checked) {
      this.state = CheckState.unchecked;
    } else {
      this.state = CheckState.checked;
    }
    if (this.children.length >= 1) {
      for (let child of this.children) {
        child.toggle();
      }
    }
  }

  check() {
    this.state = CheckState.checked;
    if (this.children.length >= 1) {
      for (let child of this.children) {
        child.check();
      }
    }
  }

  uncheck() {
    this.state = CheckState.unchecked;
    if (this.children.length >= 1) {
      for (let child of this.children) {
        child.uncheck();
      }
    }
  }
  onChangeChild(state) {}
}

/**
 * ---------------------------------------------------------
 * 채점을 위한 코드입니다.
 * 수정하면 정상적인 채점이 되지 않습니다.
 * 수정하지 말아주세요.
 * ---------------------------------------------------------
 */
function solution() {
  return { CheckItem };
}
// console.log(solution());
const res = new CheckItem({
  id: "전체 약관",
  children: [
    {
      id: "필수 약관",
      children: [{ id: "토스뱅크 대출 상품설명서", children: [] }],
    },
    {
      id: "선택 약관",
      children: [
        { id: "마케팅 푸시 알림 수신", children: [] },
        { id: "마케팅 SMS 수신", children: [] },
      ],
    },
  ],
});
console.log(res);
res.toggle();
res.uncheck();
res.check();

// console.log(JSON.stringify(res, null, 2));
