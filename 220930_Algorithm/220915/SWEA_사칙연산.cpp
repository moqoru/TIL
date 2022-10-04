#include <iostream>
//#include <fstream>
#include <string> // ��~~~~~~���� char �����δ� �� �ǰ���. string���� �մϴ�.
using namespace std;

int i, n, node, lnode, rnode, cal_a, cal_b;
int lst_l[1001], lst_r[1001], stk[1001];
string dat, lst_m[1001];
int num_stk;

void postorder(int cur) {
	if (lst_l[cur] != 0) {
		postorder(lst_l[cur]);
		postorder(lst_r[cur]);
		num_stk--; cal_b = stk[num_stk]; // ���� pop ����
		num_stk--; cal_a = stk[num_stk];
		if (lst_m[cur] == "+") {
			stk[num_stk] = cal_a + cal_b; num_stk++;
		}
		else if (lst_m[cur] == "-") {
			stk[num_stk] = cal_a - cal_b; num_stk++;
		}
		else if (lst_m[cur] == "*") {
			stk[num_stk] = cal_a * cal_b; num_stk++;
		}
		else {
			stk[num_stk] = cal_a / cal_b; num_stk++;
		}
	}
	else {
		stk[num_stk] = stoi(lst_m[cur]); num_stk++;
	}
}
int main() {
	//ifstream cin("input.txt");
	for (int cs = 0; cs < 10; cs++) {
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> node >> dat;
			lst_m[node] = dat;
			if (dat == "+" || dat == "-" || dat == "*" || dat == "/") {
				cin >> lnode >> rnode;
				lst_l[node] = lnode;
				lst_r[node] = rnode;
			}
			else {
				lst_l[node] = 0;
				lst_r[node] = 0;
			}
		}
		num_stk = 0;
		postorder(1);
		cout << "#" << cs + 1 << " " << stk[0] << endl;
	}
	//cin.close();
	return 0;
}

// 
// 1. String ��� ��� + char to String ���� ������
// 2. char ���� �ڵ� ���� ���� => �� ������ �����

// �ٺ����� ��
// 1. cout ����� ������ ó������ �� �پ ����
// 2. char �迭�� �������� �ȶ���. �⺻������ null�� �ʱ�ȭ�ż�
// ...�׳� cout �ؼ� �ٷ� ����ص� �˾Ƽ� �ڷ� ���� ������ ��µ�