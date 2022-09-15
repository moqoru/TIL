#include <iostream>
using namespace std;

int i;
char s_in[12], lst[105], ans[105];
int main() {
	
	for (int cs = 0; cs < 10; cs++) {
		int n, cnt = 0;
		cin >> n;
		cin.getline(s_in, 12); // �Ϲ� cin �ڿ� getline ������ ���� �� ���� �����ϴ�?!
		for (i = 1; i <= n; i++) {
			cin.getline(s_in, 12);
			if (i < 10)
				lst[i] = s_in[2];
			else if (i < 100)
				lst[i] = s_in[3];
			else
				lst[i] = s_in[4];
		}

		int cur = 1, ans_cnt = 0;
		while (ans_cnt < n) {
			if (lst[cur] == '\0')
				cur /= 2;
			else if (cur * 2 <= n && lst[cur * 2] != '\0')
				cur *= 2;
			else {
				ans[ans_cnt] = lst[cur];
				lst[cur] = '\0'; // NULL ���� ����
				ans_cnt++;
				if (cur * 2 + 1 <= n && lst[cur * 2 + 1] != '\0')
					cur = cur * 2 + 1;
				else
					cur /= 2;
			}
		}
		cout << '#' << cs + 1 << " ";
		for (i = 0; i < ans_cnt; i++)
			cout << ans[i];
		cout << endl;
	}
	return 0;
}

// 1. ���� ����
// 2. ���� �ڽĳ��� �� �� ����

// 
// 1. String ��� ��� + char to String ���� ������
// 2. char ���� �ڵ� ���� ����

// �ٺ����� ��
// 1. cout ����� ������ ó������ �� �پ ����
// 2. char �迭�� �������� �ȶ���. �⺻������ null�� �ʱ�ȭ�ż�
// ...�׳� cout �ؼ� �ٷ� ����ص� �˾Ƽ� �ڷ� ���� ������ ��µ�