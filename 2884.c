#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
int main() {
	int H, M;
	scanf("%d\n%d", &H, &M);
	if (M >= 45) {
		printf("%d %d", H, (M - 45));
	}
	else {//MºÐ <45
		if (H == 0) {
			M = 60 - (45 - M);
			printf("23 %d", M);
		}
		else {
			M = 60 - (45 - M);
			printf("%d %d", H - 1, M);
		}
	}

}