#include <iostream>

using namespace std;

int main() {

	int n1, n2, n3, n4, n5;
	cin >> n1 >> n2 >> n3 >> n4 >> n5;
	
	int k[14] = {};
	int var[6] = {};

	k[n1]++; k[n2]++; k[n3]++; k[n4]++; k[n5]++;
	
	for (int i = 0; i < 14; i++ ) { if (k[i]) var[k[i]]++;}

	
	if (var[5]) cout << "Impossible";
	else if (var[4]) cout << "Four of a Kind";
	else if (var[3] && var[2]) cout << "Full House";
	else if (var[1] == 5) {
		int idx = -1;
		for (int i = 0; i < 14; i++) {
			if (k[i]) {
				idx = i;
				break;
			}
		}
		
		int s = 0;
		for (int i = idx; i < idx + 5; i++ ) {
			s += k[i];
		}

		if (s == 5) cout << "Straight";
		else cout << "Nothing";
	}
	else if (var[3]) cout << "Three of a Kind";
	else if (var[2] == 2) cout << "Two Pairs";
	else if (var[2]) cout << "One Pair";
	else cout << "Nothing";
}
