#include<stdio.h>
int main() {
	int n, max, arr;
	scanf("%d %d", &n, &max);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr);
		if (arr < max) {
			printf("%d\n", arr);
		}
	}



}