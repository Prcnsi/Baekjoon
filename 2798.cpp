#include <iostream>
using namespace std;

unsigned int N, M, sum, fix, dfr,tmp,targetSum;
unsigned int arr[10000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie();
	cout.tie();

	// 숫자 입력 받기
	cin >> N >> M;
	
	// 반복문으로 N만큼의 수 입력 받기
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	// 전체 합의 경우 구하는 반복문
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
						// M이하이고 M과 가장 가까운 수 구하기 
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