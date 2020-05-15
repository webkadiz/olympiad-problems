#include <iostream>

using namespace std;

int min_diff(int *W, int n, int cur_n = 0, int pile1 = 0, int pile2 = 0) {

	if (cur_n == n)
		return abs(pile1 - pile2);

	int diff1 = min_diff(W, n, cur_n + 1, pile1 + W[cur_n], pile2);
	int diff2 = min_diff(W, n, cur_n + 1, pile1, pile2 + W[cur_n]);

	return min(diff1, diff2);
}

int main() {

	int N;
	cin >> N;

	int W[N];

	for (int i = 0; i < N; i++) {
		cin >> W[i];
	}

	int res = min_diff(W, N);

	cout << res;

	return 0;
}