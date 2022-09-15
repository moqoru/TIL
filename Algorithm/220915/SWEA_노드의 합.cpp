#include <iostream>
//#include <fstream>
using namespace std;

int t, n, m, l, in_a, in_b, i, head;
int tree[1001];

int postorder(int cur) {
	if (cur > n)
		return 0;
	else {
		if (tree[cur] == 0)
			tree[cur] = postorder(cur * 2) + postorder(cur * 2 + 1);
		return tree[cur];
	}
}

int main() {
	//ifstream cin("input.txt");
	cin >> t;
	for (int cs = 0; cs < t; cs++) {
		cin >> n >> m >> l;
		for (i = 1; i <= n; i++)
			tree[i] = 0;
		for (i = 0; i < m; i++) {
			cin >> in_a >> in_b;
			tree[in_a] = in_b;
		}
		head = postorder(1);
		cout << "#" << cs + 1 << " " << tree[l] << endl;
	}
	//cin.close();
	return 0;
}