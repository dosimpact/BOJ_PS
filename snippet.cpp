#include <stdio.h>
#include <stdlib.h>

int main()
{
    int count;
    printf("몇 개의 점수 입력\n");
    scanf_s("%d", &count);
    int *score = (int *)malloc(sizeof(int) * count);

    for (int i = 0; i < count; i++)
    {
        printf("점수입력:");
        scanf_s("%d", &score[i]);
    }
    for (int i = 0; i < count; i++)
    {
        printf("%d", *score);
        score++;
    }
}