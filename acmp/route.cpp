#include <iostream>

using namespace std;

template <typename T>
void print_arr(T arr[], int len) {
	for (int i = 0; i < len; i++) cout << arr[i] << endl;
}

int main() {

	int n;
	cin >> n;
	
	int cost[n][n];
	int dp[n][n];
	char ans[n][n];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char ch;
			cin >> ch;

			cost[i][j] = int(ch) - 48;
		}
	}

	dp[0][0] = cost[0][0];

	for (int i = 1; i < n; i++) {
		dp[0][i] = cost[0][i] + dp[0][i-1];
		dp[i][0] = cost[i][0] + dp[i-1][0];
	}

		
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < n; j++) {
			dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + cost[i][j];
		}
	}
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			ans[i][j] = '-';

	
	int k, m;
	k = m = n-1;
	ans[k][m] = '#';

	while (k || m) {
		if (k-1 < 0) {
			ans[k][m-1] = '#';
			m--;
		} else if (m-1 < 0) {
			ans[k-1][m] = '#';
			k--;
		} else if (dp[k-1][m] < dp[k][m-1]) {
			ans[k-1][m] = '#';
			k--;
		} else {
			ans[k][m-1] = '#';
			m--;
		}
	} 

	for (int i = 0; i < n; i++) {
		for (int j = 0; j< n; j++)
			cout << ans[i][j];
		
		cout << endl;
	}

}
