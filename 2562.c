#include<stdio.h>
int main() {
	int arr[10];
	int index = 1;
	//1. ���� 9�� �Է� �޴� for
	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &arr[i]);
	}
	int arr_max = arr[0];
	//2. �ݺ��ϴ� Ƚ�� �����ϴ� for��
	for (int i = 0; i < 8; i++)
	{
		// ���� �ִ� ���ϴ� if��
		if (arr_max < arr[i + 1])
		{
			arr_max = arr[i + 1];
			index = i + 2;
		}
	}
	//3.��� ���
	printf("%d\n", arr_max);
	printf("%d", index);
}