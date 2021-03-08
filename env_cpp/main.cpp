#include <iostream>
#include <algorithm>
using namespace std;

int n, m, res;
char map[20][20];

bool range_check(int y, int x, int r) {
	for (int i = -1; i <= 1; i+=2) {
		int ty = y + r * i;
		int tx = x + r * i;

		if (ty < 0 || ty >= n || tx < 0 || tx >= m) return false;
	}
	return true;
}

int other() {
	int tmp2 = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == '.') continue;

			int k = 1;
			while (range_check(i, j, k) &&
				map[i + k][j] == '#' && map[i][j + k] == '#' &&
				map[i - k][j] == '#' && map[i][j - k] == '#') {
				k++;
			}
			tmp2 = max(tmp2, (k-1) * 4 + 1);
		}
	}
	return tmp2;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == '.') continue;

			int k = 0;
			while (range_check(i, j, k) &&
				map[i + k][j] == '#' && map[i][j + k] == '#' &&
				map[i - k][j] == '#' && map[i][j - k] == '#') {
				map[i + k][j] = map[i][j + k] = map[i - k][j] = map[i][j - k] = '.';

				int tmp1 = 1 + k * 4;
				int tmp2 = other();

				res = max(res, tmp1 * tmp2);
				k++;
			}

			for (int l = 0; l < k; l++) {
				map[i + l][j] = map[i][j + l] = map[i - l][j] = map[i][j - l] = '#';
			}
		}
	}

	cout << res << '\n';

	return 0;
}