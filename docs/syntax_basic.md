## // C/C++/STL 기초

[https://docs.google.com/document/d/1xrhb-6Vm5_0zd2iImbdg_4kN2cTnY-ZSzyrFAavwABI/edit?usp=sharing](https://docs.google.com/document/d/1xrhb-6Vm5_0zd2iImbdg_4kN2cTnY-ZSzyrFAavwABI/edit?usp=sharing)

C언어

//1.1 포멧 문자열

int %d 10진수 %x 16진수 %o 8진수
long long %lld %I64d

char %c char\* %s
float %f double %lf long double %Lf

//1.2 TestCase 또는 EOF 받기

//TetsCase
int cases; cin>>cases; while(cases--){...}

//EOF 까지

while(scanf("%d %d",&a,&b)==2){...}
while(scanf("%d %d",&a,&b)!=EOF){...}
while(c = getchar() && c!= EOF){...}

// TestCase EOF 같이 있는 경우 -> 독립적으로 생각

// %c는 공백문자 ' ' = 32 와 줄바꿈 문자 '\n'=10 을 받으므로 주의!!.
// scanf안의 공백은 공백이나 줄바꿈을 무시 하게 한다. scanf("%c %c"..)

//1.3 scanf의 공백 및 줄 바꿈 처리, 한줄 입력 받기

//(1)
scanf("%d\n",&n);
scanf("%c %c %c",&x,&y,&z);
//(2)
scanf(" %c %c %c",&x,&y,&z);
//(3)
scanf("%[^\n]\n",s); // s 에 char s[] 문자배열형
//(4)
fgets() //줄바꿈 포함 한줄 입력 가능

//1.4
scanf("%[123]",s);
scanf("%[^123]",s);

//1.5 문장의 앞뒤 공백도 다 입력 받고 싶다면?
while( (c = getchar()) && c!= EOF){
print("%c",c);
}

//1.6 scanf 지정한 갯수만 입력받기
scanf("%ld",&x); //1234입력-> 1,2,3,4 1개씩 scanf
scanf("%10s",s); // 문자열 길이가 10개 (이하) 씩 받음

//1.7 scanf 형식을 만들어서 입력받기
scanf("%d,%d",&x,&y); // 10,20 이런식의 좌표를 받을 수 있음.
//주의
while(scanf(...))는 EOF입력시 리턴값이 -1 이 되어 while(참)이 되어 무한루푸에 빠질 수 있음

2. C++ 입출력 기본

//2.1 한줄 다 입력 받기
getline(cin,s); // s는 stirng 형으로

//2.2 출력시 소수점 처리하기
#include<iomanip>
setprecision(5)
fixed
eg)
double f = 3.1415926535;
cout<<setprecision(5)<<f; //앞에서 5번째까지 출력(반올림적용)

cout<<fixed<<setprecision(5)<<f; //소수점 자리부터 5번째 가지 출력(반올림 적용)

//2.3 출력 속도비교
cout<<i<<endl; //4272msec 개행 + 스트림을 flush하기때문에 많은 시간이 걸린다.
cout<<i<<'\n'; //36msec
printf("%d\n",i); //20msec

//2.4 cin/cout 속도 올리기 (scanf/printf와 혼용하지 말것!)
main바로 다음에

    cin.tie(NULL); cout.tie(NULL);
    ios_base::sync_with_stdio(false);

//2.5 C++11 의 auto
vector<int> d;
for(auto it = d.begin(); it != d.end(); it++){...}
for(auto& k:d){...}

//2.6 Range based for
vector<int> a = {1,2,3,4,5};
a.size(); // element수 반환 unsinged long long 형태
for(auto k : a){...}//값 복사 방식으로 순환
for(auto& k : a){...}//참조 방식으로 순환 // 더 좋은 성능

//2.7 C 스타일,C++ 스타일 의 string
const char cstr[] = "string"; // foreach돌리면 7번
string str = "string"; // foreach 돌리면 6번
// C스타일의 문자열에는 null이 포함되어 있기 때문 !!!

//2.8 C++ 람다 함수 Lamda Function 익명 함수(함수의 형태인데 이름이 없음)

구성 : [캡처](함수 인자){함수 내용}
eg) cout<<[](int x,int y){return x+y;}(1,2)<<"\n";

eg) auto sum = [](int x,int y){return x+y;};
sum(1,2);

eg)
auto f = [&](){..} //외부변수 모두 참조하려면 캡처에 &쓰기

    auto f = [&x,y](){...} //외부면수 x만 참조,y는 값 복사

    auto f = [&x,y]() mutable {...}// 하지만 잘 안됨..(?)

eg)
#include<functional> 에
  
 function<int(int,int)> sum = [](int,int){....}
function<int()>
function<void()>
등등의 자료형 하지만 auto 써라.
  
eg) 람다로 recursion 피보나치 구현 또는 vector에 람다 넣고 foreach돌리면서 사칙연산 해보기~

3. STL(1) 사용법

// STL = algorithm + container + function + iterator 로 구성

//3.1 pair
#include<utility> 또는 #include<vector> 또는 #include<algorithm>

pair<int,int> p1 = make_pair(10,20);
pair<int,int> p1 = pair<int,int>(10,20);
pair<int,int> p2(10,20);

p1.first 와 p1.second 로 접근

//3.2 tuple
#include<tuple>
tuple<int,int,int> t1 = make_tuple(10,20,30);
cout<<get<0>(t1)<<'\n'; //<0>안에는 변수가 못들어 간다.

//3.3 tie
#include<tuple>

eg)
int x,y,z;
tie(x,y,z) = make_tuple(1,2,3);
eg)
tie(b,a,ignore) = make_tuple(a,b,10);
tie(a,b) = make_pair(b,a); //swap한줄 구현

//3.4 vector
#include<vector>

eg)
vector<int> v1;
vector<int> v1(10); //크기 10
vector<int> v1(10,5); // 크기 10이고 초기값 전부 5
vector<int> v1 = {1,2,3}; // 초기화 리스트를 이용해서 행성

eg)
v.push_back(); v.pop_back();
v.clear(); v.resize(); v.empty(); v.size();

v.begin(); v.end(); //포인터
  
v.front(); v.back(); v[1] //값 참조

v.emplace_back(1,2) //원소가 pair인 경우

eg)
v.insert(it,<t>)//해당 위치에 , 넣을거
v.insert(it,10,<t>) // 해당 위치에, 갯수 만큼 , 넣을거
v.insert(it,d.begin(),d.end())// 해당 위치에, 넣을 첫, 넣을 끝
  
eg)
v.erase(it);//지울거 포인팅
v.erase(it.start(),it.end())//지울거 시작 - 끝
  
//3.5 deque
#include<deque>
deque<int> dq;

dq.push_back(t);
dq.push_front(t);
dq.pop_back();
dq.pop_front();

//3.6 list 이중연결 리스트 : insert와 erase는 O(1)이 걸림
#include<list>

list<int> l ={2,1,-5};
l.sort(); // 기본 : 오름차순
l.sort(greater<int>());//내림차순
l.sort([](int& u,int& v){return abs(u)<abs(v);}); //커스텀 정렬
l.reverse

//순차 컨테이너 : vector list deque
//연관 컨테이너 : set map

//3.8 set 삽입 삭제 탐색에 log(n) 걸림
#include<set>

set<int> s1;
set<int> s2 = {1,2,3,4} // 자동 오름차 정렬 저장 및 중복 제거됨
set<int,greater<int>> s3 // 자동 내림차 정렬 하기
  
eg)
s1.insert(4); // 대입
pair<set<int>::iterator, bool > result = s2.insert(4); //결과 반환(넣은 위치,성공 여부)

    s1.erase(s.begin()); //삭제
    s1[] X //set은 순서 가 아니야
    auto it = s.erase(s.begin()+1);//{1,2,3,4} -> {1,3,4}
    it = s.erase(it) //{1,3,4} -> {1,4}


eg)
set은 for 나 foreach로 순회가 가능하다. lgN

eg)
s = {1,3,5,7}
auto it = s.find(1); //{1,3,5,7} 첫번재 원소를 가르킴
//없으면 s.end()를 반환함

    s.count(7) // 원소 7이 몇개? 1개

//3.8.2 multiset: 같은 원소 여러개를 저장 가능하다.

정리)
<T>.count의 의미
map,unordered_map,set 에서는 0또는 1 (생성하지 않고 존재 유무 )
multiset 에서는 0또는 N( 존재 및 갯수)

//3.9 map - key와 value로 이루어짐
  
#include<map>
  
map<int,int> d2 = {{1,2},{3,4}};
d2.size();//2
d2[1] //2 key를 이용해서 value참조
d2[0] //0 없으면 만들어진다. key값 0 에 value 기본값

eg)
if(d2[i]){...}//존재확인 + 없으면 만들어 버림
if(d2.count(i)){..} //존재 확인만

eg)
map<int,int> d
//내용물을 iterator 로 돌기
for(auto it = d.begin(); it != d.end() ; it++){
cout<<it->first<<it->second;
}
//내용물은 pair
for(auto& p:d){
cout<<p.first<<p.second;
}
  
//컨테이너 어댑터 : stack,queu,우선큐,bitset : 앞의 자료구조로 만듬.

//3.10 stack
#include<stack>

    stack<int> s1; //기본
    deque<int> d = {1,2,3}; stack<int> s2(d); //댁을 스택으로
    stack<int,list<int>> s3; // 리스트로 스택 만들기

    s.push(<T>)
    s.pop()
    s.top()
    s.size()
    s.empty()
    s.emplace(5,6)

//3.11 queue
#include<queue>

    queue<int> q1;
    deque<int> d = {1,2,3}; queue<int> q3(d) // 댁으로도 큐 가능
    queue<int,list<int>> q2; //리스트로 큐 만들기

    q1.push(<t>)
    q1.pop()
    q1.front()
    q1.back()
    q1.size()
    q1.empty()
    q1.emplace_back()

//3.12 priority_queue - #include<queue>에 같이 동봉됨.

#include<queue>

    priority_queue<int> pq;

    pq.push()
    pq.pop()
    pq.top() //  우선 큐는 특이하게 front 가 아닌 top 이다. tree형 stack을 연상하나봄.
    pq.empty() pq.size()


eg) 우선큐는 기본적으로 오름차 순으로 정렬된다. 그럼 내림차 우선 큐는 어떻게 만드나? 1. priority_queue<int,vector<int>,greater<int>> q3; 2. 입력시 pq.push(-x); 출력시 -pq.top() // a<b 는 -a > -b 이므로 -를 붙여 반대순서로 넣고/ 출력시 -붙여 원상복귀

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

Sec4. string

//4.1 생성자.
string(char c[]);//문자열 가능
string(const char\*); //문자열(상수) 가능
string(string s); // 초기값 지정
string(); // "" 초기화
string(int,char);//갯수를 어떤 문자를

//4.2 EOF 입력

while(cin>>s){...} //EOF 기능 리턴값 T or F
while(scanf() == 2 ){...}
while(scanf() != EOF){...}
while(getline(cin,s))
while(getline(cin,s,char delimeter))// 문자열 분리, char으로 분리할 문자 넣주기
->foreach 분석하기~

//4.3 string s의 기능
s.c_str(); //printf("%s") 형으로 출력이 가능하다.
s.size();// s.size() - 1 은 unsigned long long 의 MAX 형
s.length();//의미상
s.empty();
s1 == s1 , s1 != s2, s1<s2 //같은지,다른지,사전순서인지
s1+=s2;
s.push_back(char);
s.substr(); // s.substr(2,3)//hellow면 llo

s.append(int,char);//갯수,뭐를
s.append(string);
s.append(const char\*);
s.append // 리턴형이 string이므로 chain으로 가능

s.insert(int,string);//위치 뭐를
s.insert(int,int,char);//위치,갯수,뭘
s.insert(int,string,int,int);//넣을위치, string 의, 위치, 몇개

//4.4 숫자 문자열 변환
stoi(string);
stoi(string,int,int);//? int번 문자부터 int진수로 보고 10진수로 저장??
stll

stoul
stoull
stof
stod
stld

to_string(int 나 double 또는 float)

Sec5. STL - Algorithm

#include<algorithm> : 명심 왠만해서는 범위는 [begin,end) 이다..

//#5.1 카운팅 - 조건에 맞는, 원소 수 반환 O(N)
count(begin,end,value);
count_if(begin,end,p);

//#5.2 위치 찾기 - 조건에 맞는 원소 위치 반환 O(N)
find(begin,end,value);
find_if(begin,end,p); //없으면 end() 반환

//#5.3 원소들 (조건에 맞으면 ) 값으로 채우기
fill(begin,end,value);

//#5.4 뒤집기
reverse(begin,end);

//#5.5 회전하기
rotate(begin,mid,end);
[mid,end)를 앞으로, [begin,mid)를 뒤로 위치 바꾸기.
rotate(begin,begin+1,end); //오른쪽으로 한칸씩 이동하기
rotate(begin,end-1,end); //왼쪽으로 한칸씩 이동하기

---

//#5.6 swap
swap(a,b) // int,vector<int>
swap(_(v.begin()), _(v.begin()+1) ); // 범위가 아닌, 선택이다.!!

//#5.7 unique 구간에서 연속된 값을 제거하고 하나만 만들고 다시 넣는다.
정렬 -> 유니크 -> erase
vector<int> v;
v.sort(); // 1.정렬
auto it = v.unique(v.begin(),v.end()); //2. 유니크
erase(it,v.end()); // 3. 잔존 지우기

//#5.8 정렬 sort

sort(begin,end);
sort(begin,end,cmp);

sort(begin,end,greater<int>());
sort(begin,end,cmp);
bool cmp(const int& u, const int& v){return u > v ;}
sort(begin,end,[](const int& u,const int& v){return u > v; });

eg)pair를 이용한 람다 정렬, 문자열 -> 우선 길이 내림차, 긜고 사전 오름차
sort(s.begin,s.end,[](const string& u,const string& v){
return make_pair(-u.size(),u) < make_pair(-v.size(),v) ;} );

eg) 구조체나 클래스는 sort시 함수를 작성해 주어야 함. 내부 함수 또는 cmp 외부 함수 작성.

//#5.8.2 정렬 stable_sort 같으면 정렬전 순서가 유지됨.
stable_sort(begin,end);
stable_sort(begin,end,cmp);

//#5.9 이진 탐색, 보통 커스터 직접 만드는 경우가 흔한데,
binary_search(begin,end,value); //true or false
binary_search(begin,end,value,cmp); // true or false

---

//#5.10 최대값 최솟값 찾기

min(2,3); max(2,3);
min({1,2,3,4}); max({1,2,3,4});
min(p1,p2,cmp); max(p1,p2,cmp);

eg) 가장 작은 문자열 출력
min(s1,s2,[](string u,string v){ return u.size() < v.size(); });

minmax -> min과max를 pair형태로 반환

min_element(begin,end);
min_element(begin,end,cmp);
//최대 및 최소값의 이터레이터 반환.

eg) 정렬 -> min_element

    vector<string> ss = { "a","ab","abc","abcd"};
    auto it = min_element(ss.begin(),ss.end(),[](string u, string v){return u.size() < v.size();});
    cout<<*it;

//#5.11 값 비교, 후 크거나 같은 첫 iterator 찾기

lower_bound(begin,end,val); // val 보다 크거나 같은 첫 iterator
lower_bound(begin,end,val,cmp);
upper_bound(begin,end,val); //val 보다 큰 첫 iterator
upper_bound(begin,end,val,cmp);

//#5.12 순열

next_permutation(v.begin(),v.end()); //다음 순열
prev_permutation(v.begin(),v.end()); //이전 순열
