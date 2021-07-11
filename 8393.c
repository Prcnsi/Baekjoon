#include<stdio.h>
int main() {
	int one = 0, result = 0, n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		one++;
		result = result + one;
	}
	printf("%d", result);
}