const DARK_COLOR = "#000000";
const WHITE_COLOR = "#ffffff";

const DARK_IMG_SRC = "./img/Night.png";
const WHITE_IMG_SRC = "./img/Day.png";

function DarkMode() {
  const darkModeInputEl = document.querySelector("#header input");
  const isDarkMode = darkModeInputEl.checked;
  if (isDarkMode) {
    document.querySelector("#header").style.backgroundColor = DARK_COLOR;
    document.querySelector(".container").style.backgroundColor = DARK_COLOR;
    document.querySelector("#footer").style.backgroundColor = DARK_COLOR;

    // color
    Array.from(document.querySelectorAll("p")).map((e) => {
      e.style.color = WHITE_COLOR;
    });
    Array.from(document.querySelectorAll("h4")).map((e) => {
      e.style.color = WHITE_COLOR;
    });
    Array.from(document.querySelectorAll("h5")).map((e) => {
      e.style.color = WHITE_COLOR;
    });

    document.querySelector("#faqBtn").style.color = WHITE_COLOR;
    document.querySelector("#faqBtn").style.backgroundColor = DARK_COLOR;

    document.querySelector("#mainLogo").src = DARK_IMG_SRC;
  } else {
    document.querySelector("#header").style.backgroundColor = WHITE_COLOR;
    document.querySelector(".container").style.backgroundColor = WHITE_COLOR;
    document.querySelector("#footer").style.backgroundColor = WHITE_COLOR;

    // color
    Array.from(document.querySelectorAll("p")).map((e) => {
      e.style.color = DARK_COLOR;
    });
    Array.from(document.querySelectorAll("h4")).map((e) => {
      e.style.color = DARK_COLOR;
    });
    Array.from(document.querySelectorAll("h5")).map((e) => {
      e.style.color = DARK_COLOR;
    });

    document.querySelector("#faqBtn").style.color = DARK_COLOR;
    document.querySelector("#faqBtn").style.backgroundColor = WHITE_COLOR;

    document.querySelector("#mainLogo").src = WHITE_IMG_SRC;
  }
}
