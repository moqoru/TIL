#include <iostream>
#include <string>
using namespace std;
int main()
{
	int blank = 0;
	string s;
	getline(cin, s);
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == ' ' && i != 0 && i != s.length() - 1) {
			blank++;
		}
	}
	if (s == " ") {
		cout << 0 << endl;
	}
	else {
		cout << blank + 1 << endl;
	}
	return 0;
}