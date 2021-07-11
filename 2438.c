#include<stdio.h>
int main() {
	int star;
	scanf("%d\n", &star);
	for (int i = 1; i <= star; i++) {
		for (int j = 0; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}

}