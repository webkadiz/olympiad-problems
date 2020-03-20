#include <iostream>

using namespace std;

int s, n;

void print_arr(int arr[], int len, string mark = "", char sep = '\n') {
	for (int i = 0; i < len; i++) 
		cout << arr[i] << mark << sep;
}

void print_char(char arr[], int len, string mark = "", char sep = '\n') {
	for (int i = 0; i < len; i++) 
		cout << arr[i] << mark << sep;
}

void fill_arr(int arr[], int len) {
	for (int i = 0; i < len; i++)
		cin >> arr[i];
}


int exp(int arr[], int idx, char signs[], int res) {

	if (idx == n) {

		if (res == s) {
			
			for (int i = 0; i < n-1; i++) {
				cout << arr[i];
				cout << signs[i];
			}

			cout << arr[n-1];
			cout << "=";
			cout << s;

			exit(0);
		}
		
		return res;
	}

	int el = arr[idx];

	signs[idx-1] = '+';
	exp(arr, idx + 1, signs, res + el);
	signs[idx-1] = '-';
	exp(arr, idx + 1, signs, res - el);

	return 0;

}


int main() {

	cin >> n >> s;

	int nums[n];
	char signs[n-1];	
	
	fill_arr(nums, n);

	exp(nums, 1, signs, nums[0]);

	cout << "No solution";

	return 0;
}
