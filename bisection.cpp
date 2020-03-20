#include <iostream>
#include <iomanip>

using namespace std;

double pow(double n, int p) {

	double res = n;

	for (int i = 0; i < p - 1; i++) {
		res *= n;
	}

	return res;
}

double sqrt(double n, int p) {
	double measure = n;
	double left = 0;
	double right = n;

	if (n < 1) right = 1;

	for (int i = 0; i < 200; i++) {
	
		double mid = (right + left) / 2;
		double approx = pow(mid, p);

		if (approx > measure) {
			right = mid;
		} else {
			left = mid;
		}
		
	}

	return right;
}

int main() {
	
	double a;
	int n;
	cin >> a;
	cin >> n;
		
	cout << setprecision(17);
	cout << sqrt(a, n);

	return 0;

}

