#include<stdio.h>
int main() {
	int arr[10];
	int index = 1;
	//1. 숫자 9개 입력 받는 for
	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &arr[i]);
	}
	int arr_max = arr[0];
	//2. 반복하는 횟수 지정하는 for문
	for (int i = 0; i < 8; i++)
	{
		// 실제 최댓값 구하는 if문
		if (arr_max < arr[i + 1])
		{
			arr_max = arr[i + 1];
			index = i + 2;
		}
	}
	//3.결과 출력
	printf("%d\n", arr_max);
	printf("%d", index);
}