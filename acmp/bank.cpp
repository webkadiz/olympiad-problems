#include <iostream>

using namespace std;

const int maxint = 2147482000;

int count(int *ves, int len, int cond)
{

	for (int w = 0; w < len; w++)
	{
		int m = w / 2;

		for (int i = 1; i <= m; i++)
		{
			int el = ves[i];
			int pair_el = ves[w - i];

			if (cond == 1)
			{
				if (el > 0 && pair_el > 0 && el + pair_el > ves[w])
					ves[w] = el + pair_el;
			}
			else if (cond == 0)
				if (el < maxint && pair_el < maxint && el + pair_el < ves[w])
					ves[w] = el + pair_el;
		}
	}

	return ves[len - 1];
}

int main()
{

	int E, F, N;
	cin >> E >> F >> N;

	int max_w = F - E + 1;

	int ves_max[max_w], ves_min[max_w];

	for (int i = 0; i < max_w; i++)
	{
		ves_max[i] = 0;
		ves_min[i] = maxint;
	}

	for (int i = 0; i < N; i++)
	{
		int p, w;
		cin >> p >> w;

		if (w >= max_w)
			continue;

		if (ves_max[w])
		{
			if (p > ves_max[w])	
				ves_max[w] = p;
			if (p < ves_min[w])
				ves_min[w] = p;
			continue;
		}
		ves_max[w] = p;
		ves_min[w] = p;
	}

	if (E == F)
	{
		//cout << "This is impossible.";
		cout << 0 << ' ' << 0;
		return 0;
	}

	int res_max, res_min;

	res_max = count(ves_max, max_w, 1);
	res_min = count(ves_min, max_w, 0);

	if (res_max == 0 || res_min == maxint)
		cout << "This is impossible.";
	else
		cout << res_min << ' ' << res_max;

	return 0;
}
