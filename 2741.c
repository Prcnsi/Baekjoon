#include<stdio.h>
int main() {
	long long int T;
	int num = 0;
	scanf("%lld\n", &T);
	for (int i = 1; i <= T; i++) {
		num++;
		printf("%d\n", num);
	}
}