#include <iostream>

using namespace std;

template <typename T>
void print_arr(T arr[], int len) {
	for (int i = 0; i < len; i++) cout << arr[i] << endl;
}

template <typename T>
void copy_arr(T arr_c[], T arr[], int len) {
	for (int i = 0; i < len; i++) arr_c[i] = arr[i];
}

void per(char s[], bool use[], int n, int k, char ans[]) {
	
	if (n == k) {
		for (int i = 0; i < k; i++) cout << ans[i];
		cout << endl;
		return;
	}

	for (int i = 0; i < k; i++) {		
		if (s, use[i]) continue;
		
		bool cuse[k];
		copy_arr(cuse, use, k);
		cuse[i] = true;
		
		ans[n] = s[i];

		per(s, cuse, n + 1, k, ans);

	}	
}


int main() {

	char sRaw[8];
	int k = 0;

	cin >> sRaw;

	for (int i = 0; i < 8; i++) if (sRaw[i]) k++;

	char s[k];
	char ans[k];
	bool use[k] = {};

	for (int i = 0; i < k; i++) s[i] = sRaw[i];
	
	per(s, use, 0, k, ans);
}





