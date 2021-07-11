#include<stdio.h>
int main() {
	int T;
	scanf("%d\n", &T);
	while (1) {
		printf("%d\n", T);
		T = T - 1;
		if (T <= 0) {
			break;
		}
	}
}