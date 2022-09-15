#include <iostream>
//#include <fstream>
#include <string> // 도~~~~~~저히 char 형으로는 안 되겠음. string으로 합니다.
using namespace std;

int i, n, node, lnode, rnode, cal_a, cal_b;
int lst_l[1001], lst_r[1001], stk[1001];
string dat, lst_m[1001];
int num_stk;

void postorder(int cur) {
	if (lst_l[cur] != 0) {
		postorder(lst_l[cur]);
		postorder(lst_r[cur]);
		num_stk--; cal_b = stk[num_stk]; // 스택 pop 연산
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
// 1. String 헤더 사용 + char to String 구문 익히기
// 2. char 관련 코드 새로 배우기 => 는 지금은 힘들듯

// 바보짓한 거
// 1. cout 출력은 어차피 처음부터 다 붙어서 나옴
// 2. char 배열은 생각보다 똑똑함. 기본적으로 null로 초기화돼서
// ...그냥 cout 해서 바로 출력해도 알아서 자료 넣은 곳까지 출력됨