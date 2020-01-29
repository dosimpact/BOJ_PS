//https://www.acmicpc.net/problem/5549

#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
#include <deque>
#include <vector>
#include <string>
#include <stack>
#define SIZE 1001
using namespace std;

struct JOI
{
    int j;
    int o;
    int i;
    JOI operator+(JOI &p)
    {

        return {j + p.j, o + p.o, i + p.i};
    }
};

JOI d[SIZE][SIZE];
int n, m, k;
vector<string> graph;

int main()
{
    cout << d[0][0].j;
}
