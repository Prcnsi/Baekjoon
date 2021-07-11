#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
int main() {
	int a, b, c, d, e, f;
	scanf("%1d%1d%1d\n%1d%1d%1d", &a, &b, &c, &d, &e, &f);
	printf("%d\n", (100 * a + 10 * b + c) * f);
	printf("%d\n", (100 * a + 10 * b + c) * e);
	printf("%d\n", (100 * a + 10 * b + c) * d);
	printf("%d\n", (100 * a + 10 * b + c) * (100 * d + 10 * e + f));
}