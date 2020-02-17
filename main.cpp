#include <iostream>
#include <cstdio>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 101

using namespace std;
int n, m;
vector<int> graph[SIZE];

string solution(string s, int n)
{
    string answer = "";
    //s for문 돌면서, +n만큼해줘, 단, z를 넘어서면 a로 바꿔주기
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            char tmp = s[i];
            printf("DEBUG: %d ", tmp);
            tmp += n;
            printf("DEBUG: %d ", tmp);
            if (tmp > 'z')
            {
                tmp = 'a' + (tmp - 'z') - 1;
            }
            answer += tmp;
        }
        else if (s[i] >= 'A' && s[i] <= 'Z')
        {
            char tmp = s[i];
            tmp += n;
            if (tmp > 'Z')
            {
                tmp = 'A' + (tmp - 'Z') - 1;
            }
            answer += tmp;
        }
        else
        {
            answer += ' ';
        }
    }
    return answer;
}
string caesar(string s, int n)
{
    string answer = "";

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == ' ')
        {
            answer += s[i];
        }
        else
        {
            int start = (s[i] >= 'a') ? 'a' : 'A';
            answer += start + (s[i] - start + n) % 26;
        }
    }

    return answer;
}
int main()
{

    cout << caesar("a z", 25) << '\n';
    cout << solution("a z", 25) << '\n';
}
