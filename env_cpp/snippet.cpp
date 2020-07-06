#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print2D(int arr[][10])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int arr[3][10];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            arr[i][j] = i + j;
        }
    }
    print2D(arr);
    memset(arr, -1, sizeof(arr));
    print2D(arr);
}