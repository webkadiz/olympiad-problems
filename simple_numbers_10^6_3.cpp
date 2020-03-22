#include <iostream>
#include <math.h>

using namespace std;

template <typename T>
void print_arr(T arr[], int len) {
	for (int i = 0; i < len; i++) cout << arr[i] << endl; 

}


bool detSimple(int num) {

	int sqrtN = sqrt(num);

	for (int i = 2; i <= sqrtN; i++) {
		if (num % i == 0) return false;
	}

	return true;
}

int main () {

	int m, n;
	bool wasSimple = false;
	cin >> m >> n;
	n++;

	for (int i = m; i < n; i++) {
		bool isSimple = detSimple(i);

		if (isSimple) {
			cout << i << endl;
			wasSimple = true;
		}
	}

	if (!wasSimple) cout << "Absent";


}

