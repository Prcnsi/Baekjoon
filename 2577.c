#include<stdio.h>
#pragma warning(disable:4996)
int main() {
	int jarisu = 0, n;
	int X, Y, Z;
	int digits[10] = { 0, };
	int cal_result;
	//1. ���� �� �� �Է� �ޱ�.
	scanf("%d", &X);
	scanf("%d", &Y);
	scanf("%d", &Z);
	//2. �� ������ ��(���� 0�� �� ��)
	cal_result = X * Y * Z;

	//3.�� �ڸ��� ���ڸ� ���ϴ� �ݺ���(������ ���)
	for (int i = 0; cal_result > 0; i++)
	{
		n = cal_result % 10;
		digits[n]++;
		cal_result /= 10;
	}
	//4.��� ��� �ݺ���
	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", digits[i]);
	}
}
