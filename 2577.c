#include<stdio.h>
#pragma warning(disable:4996)
int main() {
	int jarisu = 0, n;
	int X, Y, Z;
	int digits[10] = { 0, };
	int cal_result;
	//1. 숫자 세 개 입력 받기.
	scanf("%d", &X);
	scanf("%d", &Y);
	scanf("%d", &Z);
	//2. 세 숫자의 곱(몫이 0이 될 때)
	cal_result = X * Y * Z;

	//3.각 자리의 숫자를 구하는 반복문(나머지 사용)
	for (int i = 0; cal_result > 0; i++)
	{
		n = cal_result % 10;
		digits[n]++;
		cal_result /= 10;
	}
	//4.결과 출력 반복문
	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", digits[i]);
	}
}
