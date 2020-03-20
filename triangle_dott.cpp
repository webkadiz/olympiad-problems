#include <iostream>

using namespace std;

struct Point 
{
	int x;
	int y;
};

int pos(Point p1, Point p2, Point p3) {

	int dx1 = p1.x - p2.x;
	int dy1 = p1.y - p2.y;
	int dx2 = p3.x - p2.x;
	int dy2 = p3.x - p2.x;

	if (dx1 == 0) {
		if (p3.x > p1.x) { return 1; }
		else if (p3.x == p1.x) { return 0; }
		else if (p3.x < p1.x) { return -1; }
	}

	if (dx2 == 0) {
		if (p3.y > p1.y) { return 1; }
		else if (p3.y == p1.y) {return 0; }
		else if (p3.y < p1.y) { return -1; }
	}

	float k1 = dy1 / dx1;
	float k2 = dy2 / dy2;
	
	cout << k1 << ' ' << k2 << endl;
	
	if (k1 * k2 < 0) { return -1; }
	else { return 1; }


}


int main() {

	int x1, y1, x2, y2, x3, y3, x4, y4;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
	
	Point p1 {x1, y1}, p2 {x2, y2}, p3 {x3, y3}, p4 {x4, y4};
	
	int check1 = abs(pos(p1, p2, p3) - pos(p1, p2, p4));

	int check2 = abs(pos(p2, p3, p1) - pos(p2, p3, p4));

	int check3 = abs(pos(p3, p1, p2) - pos(p3, p1, p4));

	cout << check1 << check2 << check3;

	if (check3 == 2 || check2 == 2 || check1 == 2) {
		cout << "Out";
	} else {
		cout << "In";
	}

}
