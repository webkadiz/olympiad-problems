#include <iostream>

using namespace std;

int main() {

	int N;
	cin >> N;

	int arr[N];

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	int cnt_all = 0;
	for (int i = 0; i < N; i++) {
		int cnt = 0;

		for (int j = 0; j < N; j++) {
			if (arr[i] == arr[j])
				cnt += 1;
		}

		cnt_all += cnt;
	}

	if (cnt_all == N)
		cout << "All elements different";
	else
		cout << "There is equal elements";

	return 0;
}