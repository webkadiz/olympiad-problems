#include <iostream>
#include <fstream>

using namespace std;

void read_data(int arr[], int n) {
	
	for (int i = 0; i < n; i++) 
		cin >> arr[i];
}

void add_to_set(int set[], int &set_len, int elem) {

	for (int i = 0; i < set_len; i++) {
		if (set[i] == elem) return;
	}
	
	set[set_len] = elem;
	set_len++;

}

void print_arr(int arr[], int n) {
	
	cout << '[';
	for (int i = 0; i < n; i++)
		cout << arr[i] << ' ';
	cout << '\b' << ']';
}


int main() {

	int n;
	cin >> n;

	int types[n];
	int res[n] = {};	
	
	
	read_data(types, n);
	

	for (int i = 0; i < n; i++) {
		
		int set[n] = {};
		int set_len = 0;
		
		for (int j = i; j >= 0; j--) {
			add_to_set(set, set_len, types[j]);

			res[i - j] += set_len;
		}
	
	}

	for (int i = 0; i < n; i++) {
		cout << res[i] << ' ';
	}

	return 0;

}


