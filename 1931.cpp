#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N,connect,cnt;


int main() {
	// �ݺ�Ƚ�� �Է� �ޱ�
	cin >> N;

	// �ð� �� �Է� �޴� pair����
	vector<pair<int, int>> p(N);

	// pair �Է� �ޱ�
	for (int i = 0; i < N; i++)
	{
		// pair�� sort�ϸ� ù ��° ���ڸ� �������� �����ؼ� �� ��° ���� �����ϱ� ���� second�� first������ �ٲ� �Է� ����
		cin >> p[i].second >> p[i].first;
	}

	// �����½ð��� ������������ ����
	sort(p.begin(), p.end());

	// ù ��° ���� connect(0���� ����)q���� ũ�� �ش� ���̽��� second�� connect�� ��Ƽ� ����
	for (int i = 0; i < N; i++) {
		if (p[i].second >= connect) {
			connect = p[i].first;
			cnt++;
		}
	}

	cout << cnt;
}


