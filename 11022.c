#include<stdio.h>
int main() {
	int canum;
	scanf("%d\n", &canum);
	for (int i = 1; i <= canum; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d\n", i, a, b, a + b);
	}

}