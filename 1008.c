#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
int main() {
	long double a, b;
	scanf("%llf %llf", &a, &b);
	printf("%.10llf", a / b);
}