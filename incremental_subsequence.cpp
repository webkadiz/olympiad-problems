#include <iostream>

using namespace std;

void print_arr(int arr[], int len, string mark = "", char sep = '\n') {
	for (int i = 0; i < len; i++) 
		cout << arr[i] << mark << sep;
}

void fill_arr(int arr[], int len) {
	for (int i = 0; i < len; i++)
		cin >> arr[i];
}

int main() {

	int n;

	cin >> n;

	int seq[n] = {};
	int k[n] = {};

	fill_arr(seq, n);

	for (int i = 0; i < n; i++) {
		k[i] = 1;

		int best = 0;
		for (int j = i-1; j >= 0; j--) {
			if (seq[j] < seq[i] && k[j] > best) {
				best = k[j];
			} 
		}

		k[i] = best + 1;

		//cout << k[i] << ' ' << best << " best" << endl;
	}

	int mk = 0;
	int mk_idx = -1;
	for (int i = 0; i < n; i++) {
		if (k[i] > mk) {
			mk = k[i];
			mk_idx = i;
		}
	}


	int ans_seq[mk] = {};

	int cmk = mk+1;
	int ans_idx=mk-1;
	for (int i = 0; i < mk; i++) {

		for (int j = mk_idx; j >= 0; j--) {
			if (k[j] == cmk-1) {
				// cout << k[j] << ' ' << seq[j] << ' ' << j << " ans" << endl;
				ans_seq[ans_idx] = seq[j];
				cmk--;
				ans_idx--;
				mk_idx = j;
				break;
			}
		}
	}


	cout << mk << endl;
	print_arr(ans_seq, mk, "", ' ');

}