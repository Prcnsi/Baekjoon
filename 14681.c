#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
int main() {
	int x, y;
	scanf("%d\n%d", &x, &y);
	if (x > 0) {
		if (y > 0) {
			printf("1");
		}
		else {
			printf("4");
		}
	}
	if (x < 0) {
		if (y > 0) {
			printf("2");
		}
		else {
			printf("3");
		}
	}

}