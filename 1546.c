#include<stdio.h>
int main() {
	int a;
	float cnt = 0, init = 0, tmp = 0;
	float arr[1001] = { 0,0,0,0 };
	scanf("%d", &a);
	for (int i = 0; i < a; i++)
	{
		scanf("%d", &arr[i]);
	}
	init = arr[0];
	for (int i = 0; i < a; i++)
	{
		if (init < arr[i])
		{
			init = arr[i];
		}
	}
	for (int i = 0; i < a; i++)
	{
		arr[i] = (arr[i] / init) * 100;
		tmp = tmp + arr[i];
	}
	printf("%f", tmp / a);
}