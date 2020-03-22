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


int main() {

	int m, n, k = 0, sqrtN;
	bool wasSimple = false;
	
	cin >> m >> n;
	n++;
	
	sqrtN = sqrt(n);
	
	bool primesRaw[sqrtN];
	primesRaw[0] = primesRaw[1] = false;

	for (int i = 2; i <= sqrtN; i++) {
		bool isSimple = detSimple(i);
		
		k += isSimple;
		primesRaw[i] = isSimple;

	}
	
	int primes[k];

	for (int i = 2, j = 0; i <= sqrtN; i++) {
		if (primesRaw[i]) {
			primes[j] = i;
			j++;
		}
	}
	

	if (m <= sqrtN) {
		for (int i = m; i <= sqrtN; i++) {
			bool isSimple = detSimple(i);
			
			if (isSimple) {
				cout << i << endl;
				wasSimple = true;
			}
		}
	}

	for (int i = max(m, sqrtN + 1); i < n; i++) {
		bool isSimple = true;

		for (int j = 0; j < k; j++) {
			if (i % primes[j] == 0) {
				isSimple = false;
				break;
			}
		}
		
		if (isSimple) {
			wasSimple = true;
			cout << i << endl;
		}

	}
	
	if (!wasSimple) cout << "Absent";


}


