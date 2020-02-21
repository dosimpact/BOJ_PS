#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;
int n, m, cnt = 0; //책의 개수, 한번에 들 수 있는 책의 수, 총 움직인 거리
vector<int> v;     //책의 위치

/*한번 움직일 때 m만큼 들고 이동. 
책을 모두 제자리에 놓은 뒤 다시 시작지점으로 돌아올 필요 없음.
그러므로 가장 먼 곳에 놓아야 하는 책은 왕복X */

int main()
{
    cin >> n >> m; //n,m 입력
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        v.push_back(a);
    } //위치(좌표) 입력

    sort(v.begin(), v.end()); //가장 작은 수가 왼쪽에, 가장 큰 수가 오른쪽에 오도록 정렬

    if (abs(v.front()) >= abs(v.back())) //가장 먼 음수좌표의 거리가 가장 먼 양수좌표의 거리보다 멀 경우
    {
        cnt += abs(v.front());                            //가장 멀리 떨어진 음수좌표 거리만큼 이동 (왕복x)
        for (int i = m; v[i] < 0 && i < v.size(); i += m) //음수좌표를 왔다갔다 할 때 반복
        {
            cnt += abs(v[i]) * 2;
        }
        for (int i = v.size() - 1; v[i] > 0 && i >= 0; i -= m) //양수좌표를 왔다갔다 할 때 반복
        {
            cnt += v[i] * 2;
        }
    }
    else //가장 먼 음수좌표의 거리가 가장 먼 양수좌표의 거리보다 멀지않을 때
    {
        cnt += abs(v.back());                             //가장 먼 거리 이동 (왕복x)
        for (int i = 0; v[i] < 0 && i < v.size(); i += m) //음수좌표를 왔다갔다 할 때 반복
        {
            cnt += abs(v[i]) * 2;
        }
        for (int i = (v.size() - 1) - m; v[i] > 0 && i >= 0; i -= m) //양수좌표를 왔다갔다 할 때 반복
        {
            cnt += v[i] * 2;
        }
    }
    cout << cnt << endl; //출력
    return 0;
}
