## C/C++/STL 기초 to Python

# Section1. 변수 연산 입력 출력

[# Section2. 시퀀스 데이터 자료 구조](pythonBasic/Section1.md)

# Section2. 시퀀스 데이터 자료 구조

[# Section2. 시퀀스 데이터 자료 구조](pythonBasic/Section1.md)

## 주의!

1. input() 말고 sys.stdin.readline() 를 사용하자.

2. 재귀함수가 있는 경우, 최대 재귀 깊이를 설정해줘야 한다.

```
import sys sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

```

//2.2 출력시 소수점 처리하기
#include<iomanip>
setprecision(5)
fixed
eg)
double f = 3.1415926535;
cout<<setprecision(5)<<f; //앞에서 5번째까지 출력(반올림적용)

cout<<fixed<<setprecision(5)<<f; //소수점 자리부터 5번째 가지 출력(반올림 적용)

//3.13 bitset

//vector<bool> 형태 , 1bit만 사용한다.

bitset<10> b2(88) //10자리 2진수를 만드는데, 십진수 88을 넣을꺼임
bitset<10> b2("10010")//10자리 2진수를 만드는데, 2진수 10010을 넣을꺼임
bitset<n> b2 // 애러

    bitset<100000>a;
    bitset<100000>b;

    cin >> a >> b;

    cout << (a & b) << '\n'; //AND
    cout << (a | b) << '\n'; //OR
    cout << (a ^ b) << '\n';	//XOR
    cout << ~(a) << '\n';	//NOT
    cout << ~(b);		//NOT

eg)참조

b2[i]
b2.test(i)

b.flip() b.flip(1) // 0 => 1, 1 => 0
b.set() b.set(1) // 0,1 => 1로
b.reset() b.reset(1) //0,1 => 0으로

b.all() //모두 1?
b.any() //적어도 한개는 1?
b.none() //모두 0?
b.count()//1이 몇개인가?

//삽입 삭제 시간 --> 백터는 N , set은 lgN, 리스트는 1
//count의 의미 set에서는 존재성 / multiset 에서는 갯수 / STL의 count도 갯수, map,unordered_map에서 존재성

Sec5. STL - Algorithm

//#5.9 이진 탐색, 보통 커스터 직접 만드는 경우가 흔한데,
binary_search(begin,end,value); //true or false
binary_search(begin,end,value,cmp); // true or false

---

//#5.12 순열

next_permutation(v.begin(),v.end()); //다음 순열
prev_permutation(v.begin(),v.end()); //이전 순열
