#include<stdio.h>
int main() {
	int num[10];
	int result = 0;
	//1. 숫자 10개 입력 받고 나머지 구하기
	for (int i = 0; i < 10; i++)
	{
		scanf("%d", &num[i]);
		num[i] = num[i] % 42;
	}

	//2. 이중 반복문으로 독립되는 한 수 셈
	for (int i = 0; i < 10; i++) {
		int standard = 0;
		for (int j = i + 1; j < 10; j++)
		{
			if (num[i] == num[j])
			{
				standard++;
			}
		}
		if (standard == 0)
		{
			result++;
		}
	}
	printf("%d", result);

}