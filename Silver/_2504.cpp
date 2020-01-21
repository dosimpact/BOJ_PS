//https://www.acmicpc.net/problem/2504
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <stack>
using namespace std;
string in;
int main()
{
    cin >> in; //괄호 넣고
    stack<char> st;
    for (int i = 0; i < in.size(); i++) // 괄호를 돌면서
    {
        //(,[ 인 경우에는 무조건 넣는다.
        if (in[i] == '(' || in[i] == '[')
        {
            st.push(in[i]);
        }
        //( X.. ) 인경우에는 , X..값들을 더해주고, *2를 해준다. 중간에 [가 나오거나, 없는경우있음.
        else
        {
            if (in[i] == ')')
            {
                int X = 0;
                // ( 가 나올떄까지 뺀다. 숫자는 더해주고,
                while (true)
                {
                    if (st.empty() || st.top() == '[')
                    {
                        cout << 0;
                        return 0;
                    }
                    if (st.top() == '(')
                    {
                        st.pop();
                        break;
                    }
                    int t = st.top();
                    X += (t - '0');
                    st.pop();
                }
                X == 0 ? X = 1 : X = X;
                X *= 2;
                st.push(X + '0');
            }
            else if (in[i] == ']')
            {
                int Y = 0;
                // ) 가 나올떄까지 뺀다. 숫자는 더해주고,
                while (true)
                {
                    if (st.empty() || st.top() == '(')
                    {
                        cout << 0;
                        return 0;
                    }
                    if (st.top() == '[')
                    {
                        st.pop();
                        break;
                    }
                    int t = st.top();
                    Y += t - '0';
                    st.pop();
                }
                Y == 0 ? Y = 1 : Y = Y;
                Y *= 3;
                st.push(Y + '0');
            }
        }
    }
    int ans = 0;
    while (!st.empty())
    {
        if (st.top() == '(' || st.top() == '[')
        {
            cout << 0;
            return 0;
        }
        ans += st.top() - '0';
        //cout << st.top() - '0' << " ";
        st.pop();
    }
    cout << ans;
}
