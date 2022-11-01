#include <iostream>
#include <string>
using namespace std;
int main()
{
	int i, alpha[26];
	for (i = 0; i < 26; i++)
		alpha[i] = 0;
	string S;
	getline(cin, S);
	for (i = 0; i < S.length(); i++) {
		int N = int(S[i]);
		if (int('a') <= N && N <= int('z'))
			alpha[N - int('a')]++;
		else if (int('A') <= N && N <= int('Z'))
			alpha[N - int('A')]++;
	}
	int myMax = 0, same = 0, idx = -1;
	for (i = 0; i < 26; i++) {
		if (alpha[i] > myMax) {
			myMax = alpha[i];
			idx = i;
			same = 1;
		}
		else if (alpha[i] == myMax)
			same++;
	}
	if (same != 1)
		cout << '?' << endl;
	else
		cout << char('A' + idx) << endl;
	return 0;
}