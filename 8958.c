#include<stdio.h>
#include<string.h>
#define SIZE 80
int calcul_score(char a[SIZE + 1])
{
	int score = 0;
	int score_len = 0;
	int nujeoak = 0;
	int cnt;
	for (int i = 0; i < strlen(a); i++)
	{
		cnt = 1;
		if (a[i] == 'O')
		{
			cnt = cnt + nujeoak;
			score += cnt;
			nujeoak++;
		}
		else
		{
			nujeoak = 0;
		}
	}
	return score;
}
int main() {
	char save_score[SIZE + 1];
	int test_num = 0;
	int final_score;
	scanf("%d", &test_num);
	for (int i = 0; i < test_num; i++)
	{
		scanf("%s", save_score);
		final_score = calcul_score(save_score);
		printf("%d\n", final_score);
	}
}