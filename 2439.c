#include<stdio.h>
int main() {
	int star;
	scanf("%d", &star);
	for (int i = 1; i <= star; i++) {
		int bosu = 1;
		for (int j = star - 1; j >= i; j--) {
			printf(" ");
		}

		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}
}