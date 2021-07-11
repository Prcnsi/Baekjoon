#include<stdio.h>
int main() {
	int weight = 0, count = 0;
	scanf("%d", &weight);
	while (1)
	{
		if (weight % 5 == 0)
		{
			count += weight / 5;
			printf("%d", count);
			break;
		}
		weight = weight - 3;
		count++;
		if (weight < 0)
		{
			printf("-1");
			break;
		}
	}
}