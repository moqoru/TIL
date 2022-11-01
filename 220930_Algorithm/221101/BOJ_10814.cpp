#include <iostream>
#include <string>
#include <algorithm>
#define MAX_INPUT 100001
using namespace std;
class People {
public:
	int age, num;
	string name;
	People(int num, int age, string name) {
		this->num = num;
		this->age = age;
		this->name = name;
	}
	People() {}
};

bool cmp(People a, People b) {
	if (a.age == b.age)
		return a.num < b.num;
	else
		return a.age < b.age;
}
int main()
{
	int i, Age, N;
	string Name;
	cin >> N;
	People P[MAX_INPUT];
	for (i = 0; i < N; i++) {
		cin >> Age >> Name;
		P[i] = People(i, Age, Name);
	}
	sort(P, P + N, cmp);
	for (i = 0; i < N; i++) {
		cout << P[i].age << " " << P[i].name << "\n";
	}
	return 0;
}