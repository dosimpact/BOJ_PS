console.log("main.js");

const emailEl = document.querySelector("#email")
const genderEl = document.querySelector("#gender")
const nameEl = document.querySelector("#name")
const pictureEl = document.querySelector("#picture")


const fetchData = async ()=>{
    const response = await fetch("https://randomuser.me/api/")
    const data = await response.json()
    return data    
}

const main = async()=>{
    const {results} = await fetchData();
    const {email,gender,picture,name} = results[0]
    console.log(email,gender,picture,name);
    emailEl.textContent = `email : ${email}`
    genderEl.textContent = `gender : ${gender}`
    nameEl.innerHTML = `name : ${name["title"]}.${name["first"]} ${name["last"]}`
    pictureEl.setAttribute('src',picture.medium)
}

main()