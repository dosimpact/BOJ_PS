#include <iostream>
using namespace std;
int d[100002];
int p[100002];

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		int tmp;
		cin >> tmp;
		p[i] = tmp;
	}

	d[1] = p[1];

	for (int i = 2; i <= n; i++)
	{
		d[i] = p[i];
		if (d[i - 1] + p[i] > d[i])
		{
			d[i] = d[i - 1] + p[i];
		}
	}
	int ans = -1001;
	for (int i = 1; i <= n; i++)
	{
		if (ans < d[i])
			ans = d[i];
	}
	cout << ans << "\n";

	return 0;
}