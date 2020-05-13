#include <iostream>
#include <math.h>

using namespace std;

int main() {
	
	int n, sqrtN;
	cin >> n;

	sqrtN = sqrt(n);
	
	int muls[sqrtN+1] = {};

	for (int d = 2; d <= sqrtN; d++) {
	
		while (n % d == 0) {
			muls[d]++;
			n /= d;
		}
	
	}
	
	bool wasStart = false;
	for (int i = 2; i <= sqrtN; i++) {
		for (int j = 0; j < muls[i]; j++) {
			if (wasStart) {
				cout << '*' << i;
			}
			else {
				cout << i;
				wasStart = true;
			}
		}
	}

	if (n!=1) {
		if (wasStart) {
			cout << '*' << n;
		} else {
			cout << n;
		}
	}

}
