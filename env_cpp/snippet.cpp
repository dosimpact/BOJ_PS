#include <iostream>
#include <string>
#include <iomanip>
#include <vector>

#define endl "\n";

using namespace std;

int main(int argc, char *argv[])
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    vector<int> d;
    d.push_back(10);
    d.push_back(20);
    d.push_back(30);
    for (auto &k : d)
    {
        cout << k << "\n";
    }
    cout << d.size() << "\n";

    // const char cstr[] = "string";
    string str = "string";
    cout << str << endl;

    return 0;
}