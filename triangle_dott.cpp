#include <iostream>

using namespace std;

long long pos(int x1, int y1, int x2, int y2, int x3, int y3) {
	return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);
}

int main() {

	int x1, y1, x2, y2, x3, y3, x4, y4;
	long long cond1, cond2, cond3;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;

	cond1 = pos(x1, y1, x2, y2, x3, y3) * pos(x1, y1, x2, y2, x4, y4);
	cond2 = pos(x2, y2, x3, y3, x1, y1) * pos(x2, y2, x3, y3, x4, y4);
	cond3 = pos(x1, y1, x3, y3, x2, y2) * pos(x1, y1, x3, y3, x4, y4);
	
	if (cond1 >= 0 && cond2 >= 0 && cond3 >= 0) cout << "In";
	else cout << "Out";

}
