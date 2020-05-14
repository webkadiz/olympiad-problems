#include <iostream>

using namespace std;

int main() {

	int N, K;
	cin >> N >> K;

	int cnt_arr[N];

	cnt_arr[0] = K-1;
	cnt_arr[1] = K*(K-1);

	for (int i = 2; i < N; i++) {
		cnt_arr[i] = (K-1)*cnt_arr[i - 1] + (K-1)*cnt_arr[i - 2];
	}

	cout << cnt_arr[N-1];
}