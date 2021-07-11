#include<stdio.h>
#include<stdlib.h>
int main() {
	int n, max, low;
	scanf("%d", &n);
	int* arr = NULL;
	arr = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	max = *arr;
	low = *arr;
	for (int i = 0; i < n - 1; i++)
	{
		if (arr[i] < arr[i + 1])
		{
			if (arr[i + 1] > max) {
				max = arr[i + 1];
			}
			if (arr[i] < low) {
				low = arr[i];
			}
		}
		else {//arr[i]>arr[i+1]
			if (arr[i] > max) {
				max = arr[i];
			}
			if (arr[i + 1] < low) {
				low = arr[i + 1];
			}
		}
	}
	printf("%d %d", low, max);
	free(arr);
}