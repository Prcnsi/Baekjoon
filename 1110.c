#include<string.h>
#include<stdio.h>
int main() {
	int a, b, c, d, ct = 0, n, re;
	scanf("%d", &n);
	re = n;
	while (1) {
		a = n / 10;
		b = n % 10;//일의자리
		c = (a + b) % 10;
		d = 10 * b + c;
		n = d;
		ct++;
		if (re == d) {
			break;
		}
	}
	printf("%d", ct);
}//cycle힘수에서 a에 십의자리,b에 일의자리
