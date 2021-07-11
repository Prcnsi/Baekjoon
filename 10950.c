#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
int main() {
	int A, B, T;
	int c = 0;
	scanf("%d\n", &T);
	for (int i = 1; i <= T; i) {
		scanf("%d %d", &A, &B);
		printf("%d\n", A + B);
		c++;
		if (c == T) {
			break;
		}
	}
}