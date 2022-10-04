#include <iostream>
using namespace std;

int i;
char s_in[12], lst[105], ans[105];
int main() {
	
	for (int cs = 0; cs < 10; cs++) {
		int n, cnt = 0;
		cin >> n;
		cin.getline(s_in, 12); // 일반 cin 뒤에 getline 구문을 쓰면 한 줄이 씹힙니다?!
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
				lst[cur] = '\0'; // NULL 문자 삽입
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

// 1. 값이 없음
// 2. 왼쪽 자식노드로 갈 수 있음

// 
// 1. String 헤더 사용 + char to String 구문 익히기
// 2. char 관련 코드 새로 배우기

// 바보짓한 거
// 1. cout 출력은 어차피 처음부터 다 붙어서 나옴
// 2. char 배열은 생각보다 똑똑함. 기본적으로 null로 초기화돼서
// ...그냥 cout 해서 바로 출력해도 알아서 자료 넣은 곳까지 출력됨