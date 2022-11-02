#include <iostream>
using namespace std;
int N, M, ansSum = -1;
int Deck[101];
void nCr(int idx, int cnt, int nowSum) {
	//cout << idx << " " << cnt << " " << nowSum << '\n';
	if (cnt >= 3) {
		if (M - nowSum < M - ansSum)
			ansSum = nowSum;
	}
	else {
		for (int i = idx + 1; i < N - 2 + cnt; i++) {
			if (nowSum + Deck[i] <= M)
				nCr(i, cnt + 1, nowSum + Deck[i]);
		}
	}
}
int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> Deck[i];
	}
	nCr(-1, 0, 0);
	cout << ansSum << '\n';
	return 0;
};