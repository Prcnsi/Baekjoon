#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
int main() {
	int n;
	scanf("%d\n", &n);
	for (int i = 1; i <= 9; i++) {
		printf("%d * %d = %d \n", n, i, n * i);
	}

}