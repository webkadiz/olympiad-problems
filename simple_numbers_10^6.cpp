#include <iostream>
#include <math.h>

using namespace std;

int main() {
	
	int m, n;
	cin >> m >> n;
	
	n++;

	bool primes[n];
	primes[0] = primes[1] = false;
	for (int i = 2; i < n; i++) primes[i] = 1;
	
	int sqrtN = sqrt(n) + 1;
	
	for (int i = 0; i < sqrtN; i++) {
		if (primes[i]) {
			for (int j = i*i; j < n; j += i) {
				primes[j] = false;
			}
		}
	}
	
	bool wasSimple = 0;
	
	for (int i = m; i < n; i++) {
		if (primes[i]) {
			wasSimple = 1;
			cout << i << endl;
		}
	}

	if (!wasSimple)
		cout << "Absent";
	

}


