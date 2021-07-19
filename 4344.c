#include<stdio.h>
int main() {
	int case_num = 0;
	int score_num = 0;
	float score[1000];
	float score_avg = 0;
	float upper_cnt = 0;
	scanf("%d", &case_num);
	for (int i = 0; i < case_num; i++)
	{
		upper_cnt = 0;
		score_num = 0;
		score_avg = 0;
		scanf("%d", &score_num);
		for (int i = 0; i < score_num; i++)
		{
			scanf("%f", &score[i]);
			score_avg += score[i];
		}
		score_avg /= score_num;
		for (int i = 0; i < score_num; i++)
		{
			if (score_avg < score[i])
			{
				upper_cnt++;
			}
		}
		printf("%.3f%%\n", (upper_cnt / score_num) * 100);
	}
}