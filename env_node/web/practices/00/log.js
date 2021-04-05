
const data1 = ['a','b','c','d']
const data2 = {
    name:"dodo",
    age:24,
    id:"ypd03008",
    password:"sw1234"
}
// 반복문  1 - 전통 for
for (let i = 0 ; i < data1.length ; i++){
    // console.log(data1[i]);
}

// 반복문 2 - foreach
data1.forEach((data)=>{
    console.log(data);
})

// 반복문 3 - for in - [[Enumerable]]
for(const key in data2){
    console.log(key,data2[key]);
}

// 반목문 4 - for of  - Symbol.iterable
for(const data of data1){
    console.log(data);
}
// 반복분 4.2 - for of + entries 
for( const [i,data] of data1.entries()){
    console.log(i,data);
}