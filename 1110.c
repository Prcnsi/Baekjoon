#include<string.h>
#include<stdio.h>
int main() {
	int a, b, c, d, ct = 0, n, re;
	scanf("%d", &n);
	re = n;
	while (1) {
		a = n / 10;
		b = n % 10;//�����ڸ�
		c = (a + b) % 10;
		d = 10 * b + c;
		n = d;
		ct++;
		if (re == d) {
			break;
		}
	}
	printf("%d", ct);
}//cycle�������� a�� �����ڸ�,b�� �����ڸ�
