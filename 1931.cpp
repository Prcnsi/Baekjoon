#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N,connect,cnt;


int main() {
	// 반복횟수 입력 받기
	cin >> N;

	// 시간 쌍 입력 받는 pair선언
	vector<pair<int, int>> p(N);

	// pair 입력 받기
	for (int i = 0; i < N; i++)
	{
		// pair를 sort하면 첫 번째 인자를 오름차순 정렬해서 두 번째 값을 정렬하기 위해 second와 first순서를 바꿔 입력 받음
		cin >> p[i].second >> p[i].first;
	}

	// 끝나는시간을 오름차순으로 정렬
	sort(p.begin(), p.end());

	// 첫 번째 수가 connect(0으로 시작)q보다 크면 해당 케이스의 second를 connect에 담아서 갱신
	for (int i = 0; i < N; i++) {
		if (p[i].second >= connect) {
			connect = p[i].first;
			cnt++;
		}
	}

	cout << cnt;
}


