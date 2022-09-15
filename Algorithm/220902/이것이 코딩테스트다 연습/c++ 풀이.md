# 큰 수의 법칙

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int n, m, k, divk, modk;
    cin >> n >> m >> k;
    int lst[n];
    for (int i=0; i<n; i++){
        cin >> lst[i];
    }
    sort(lst, lst+n, greater<int>()); // sort 함수 연습중...
    divk = m / (k + 1); // c에서는 int형을 int형으로 나누면 자동으로 버림 처리됨.
    modk = m % (k + 1);
    cout << lst[0] * (k * divk + modk) + lst[1] * divk << endl;
}
```



# 숫자 카드 게임

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int n, m;
    int ans = 0;
    cin >> n >> m;
    int lst[m];
    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++){
            cin >> lst[j];
        }
        sort(lst, lst+m);
        if (ans<lst[0]) {ans=lst[0];}
    }
    cout<<ans<<endl;
}
```



#  1이 될 때까지

```cpp
#include <iostream>
using namespace std;
int main(){
    int n, k;
    cin >> n >> k;
    int cnt = 0;
    while (n > 1){
        if (!(n % k)) { n/=k; }
        else { n--; }
        cnt++;
    }
    cout << cnt << endl;
    return 0;
}
```



# 음료수 얼려 먹기

- 먼저 포인터 연습

```cpp
#include <iostream>
using namespace std;

int *pa;

int main()
{
    int a = 1;
    pa = &a; // &는 그 변수의 주소값, *는 그 주소가 가리키는 변수
    a = 2;
    cout << *pa << endl;
}
```

- 1번째, STL의 vector를 이용하는 방법
  - 장점 : 메모리 관리를 알아서 해 주기 때문에 메모리 해제 구문을 쓸 필요가 없음, 호출할 때 배열의 이름만 써야 한다는 것만 주의하면 다차원 배열 형태 그대로 쓸 수 있음
  - 단점 : 다차원 배열을 할당할 때 필수적으로 for문을 사용해야 함 (한 차원씩 따로 따로 할당을 개별적으로 해야 함)


```cpp
// 동적 배열 할당 풀이 #1, STL의 벡터 헤더를 이용하는 방법
#include <iostream> 
#include <string>
#include <vector>
using namespace std;

int n, m;
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, -1, 0, 1 };
void chunk(int x, int y, vector<vector<int>> &lst) {
	for (int di = 0; di < 4; di++) {
		int nx = x + dx[di];
		int ny = y + dy[di];
		if (0 <= nx && nx < n && 0 <= ny && ny < m && !(lst[nx][ny])) {
			lst[nx][ny] = 1;
			chunk(nx, ny, lst);
		}
	}
}
int main()
{
	int cut_int, i, j;
	string line_in, cut_str;
	vector<vector<int>> lst; // 먼저 선언 해줌. 다른 함수로 넘어가도 쓸 수 있으므로 전역으로 선언할 필요 없음!
	cin >> n >> m;
	lst.resize(n, 0); // 1차원씩 차례대로 동적 할당
	for (vector<int>& sub : lst)
		sub.resize(m, 0);
	// 만일 n m을 받고 선언과 동시에 초기화를 하고 싶다면 아래 구문 한 줄만 사용
	// vector<vector<int>> lst(n, vector<int>(m, 0));

	for (i = 0; i < n; i++) {
		cin >> line_in;
		for (j = 0; j < m; j++) {
			cut_str = line_in.substr(j, 1); // 문자열로 한번 받고 자른 뒤 숫자로 변환하여 2차원 배열에 저장. 
			cut_int = stoi(cut_str);
			lst[i][j] = cut_int;
		}
	}


	int cnt = 0;

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			if (!(lst[i][j])) {
				chunk(i, j, lst); // 여기서는 배열 이름만 써서 넘겨줄 것!
				cnt++;
			}
		}
	}
	cout << cnt << endl;

	return 0;
}
```



- 2번째, 1차원 배열로 바꿔준 뒤 new와 delete로 평범하게(?) 해결하는 방법

  - 장점 : 구문의 길이가 짧아짐

  - 단점 : 위치를 참조할 때 [x + 가로길이 + y]로 참조해야 하므로 복잡해짐, **delete를 하지 않으면 메모리 누수가 발생함**

```cpp
// 동적 배열 할당 풀이 #2, 동적 할당을 하되 1차원으로 변형한 배열을 이용하는 방법

#include <iostream> 
#include <string>
using namespace std;

int n, m;
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, -1, 0, 1 };
void chunk(int x, int y, int* lst) {
	for (int di = 0; di < 4; di++) {
		int nx = x + dx[di];
		int ny = y + dy[di];
		if (0 <= nx && nx < n && 0 <= ny && ny < m && !(lst[nx*m + ny])) {
			lst[nx*m + ny] = 1;
			chunk(nx, ny, lst);
		}
	}
}
int main()
{
	int cut_int, i, j;
	string line_in, cut_str;
	cin >> n >> m;
	int *lst = new int[n * m]; // 1차원 배열처럼 할당.

	for (i = 0; i < n; i++) {
		cin >> line_in;
		for (j = 0; j < m; j++) {
			cut_str = line_in.substr(j, 1); // 문자열로 한번 받고 자른 뒤 숫자로 변환하여 2차원 배열에 저장. 
			cut_int = stoi(cut_str);
			lst[i*m + j] = cut_int;
		}
	}

	for (int k = 0; k < n; k++) {
		for (int l = 0; l < m; l++)
			cout << lst[k * m + l] << " ";
		cout << endl;
	}

	int cnt = 0;

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			if (!(lst[i*m + j])) {
				chunk(i, j, lst); // 여기서는 배열 이름만 써서 넘겨줄 것!
				cnt++;
			}
		}
	}
	cout << cnt << endl;

	delete lst; // 메모리 해제 주의!!!!!!!!!!!
	return 0;
}
```

## 미로 탈출

```cpp
// 일단은 큐 헤더를 사용하지 않고, 배열만으로 풀어보겠습니다. (구식 풀이법이므로 권장하지 않습니다.)
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
	int n, m, i, j, x, y, nx, ny;
	string line_in;
	int dx[4] = { 1, 0, -1, 0 };
	int dy[4] = { 0, 1, 0, -1 };
	cin >> n >> m;
	int* qx = new int[n * m]; // 배열을 큐 대신 써보겠습니다. 우선 배열 동적 할당. c++에서는 new 구문을 써야만 가능함
	int* qy = new int[n * m]; // 최악의 경우 2차원 배열의 모든 위치가 큐에 한번씩은 들어갈 수 있으므로, 딱 배열 전체 크기만큼 만들어줍니다.
	int head = 0; // 원소가 저장된 큐의 머리 부분 위치 = 큐에서 데이터가 들어가 있는 부분 중 제일 앞 부분
	int qlen = 1; // 큐에 저장된 원소의 갯수
	qx[head] = 0; qy[head] = 0;
	vector<vector<int>> lst(n, vector<int>(m));
	for (i = 0; i < n; i++) {
		cin >> line_in;
		for (j = 0; j < m; j++) {
			lst[i][j] = stoi(line_in.substr(j, 1));
		}
	}
	lst[0][0] = 2;
	while (qlen) { // 큐에 저장된 원소 갯수가 1 이상이면 true로 동작합니다.
		x = qx[head]; y = qy[head]; // dequeue에 해당하는 구문입니다.
		qx[head] = 0; qy[head] = 0; // 앞쪽 원소가 빠져도 그 공간이 그대로 남으므로 0을 넣어 비워줍니다.
		head++; qlen--; // 큐에 새 원소가 들어갈 위치를 갱신 + 큐에 저장된 원소 갯수 줄임
		for (i = 0; i < 4; i++) {
			nx = x + dx[i]; ny = y + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m && lst[nx][ny] == 1) {
				qx[head + qlen] = nx; qy[head + qlen] = ny; // enqueue에 해당하는 구문입니다. 시작 부분 + 큐의 길이로 넣을 곳을 찾습니다.
				qlen++; // 큐에 저장된 원소 갯수 늘림
				lst[nx][ny] = lst[x][y] + 1;
				if (nx == n - 1 && ny == m - 1) {
					x = nx; y = ny; break;
				}
			}
		}
		if (nx == x && ny == y) break;
	}
	cout << lst[n - 1][m - 1] - 1 << endl;
	delete qx, qy;
	return 0;
}
```

