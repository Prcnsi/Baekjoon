#include <iostream>
using namespace std;

unsigned int N, M, sum, fix, dfr,tmp,targetSum;
unsigned int arr[10000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie();
	cout.tie();

	// ���� �Է� �ޱ�
	cin >> N >> M;
	
	// �ݺ������� N��ŭ�� �� �Է� �ޱ�
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	// ��ü ���� ��� ���ϴ� �ݺ���
	for (int i = 0; i < sizeof(arr); i++)
	{
		if (i == sizeof(arr) - 3)
		{
			break;
		}

		for (int j = i+1; j < sizeof(arr);j++)
		{
			fix = arr[i] + arr[j];
			for (int k = j+1; k < sizeof(arr); k++)
			{
				sum = fix + arr[k];
						// M�����̰� M�� ���� ����� �� ���ϱ� 
		tmp = M - sum;
		if ((tmp < dfr) && (M <=sum))
		{
			dfr = tmp;
			targetSum = sum;
		}
			}
		}

	}
	
	cout << targetSum;
	return 0;
}