#include <string.h>
#include <stdio.h>

//함수를 작성해 보자

void function(char *command, char **sArr)
{
    int j;
    char *str, *next_ptr;
    for (int i = 0; i < 10; i++)
    {
        sArr[i] = NULL;
    }

    for (j = 0, str = command;; str = NULL, j++)
    {
        sArr[j] = strtok_r(str, " ", &next_ptr);
        if (sArr[j] == NULL)
            break;
    }
    for (int i = 0; i < 10; i++)
    {
        if (sArr[i] != NULL)
            printf("%s\n", sArr[i]);
    }
    return;
}

int main(int argc, char **argv)
{

    char command[] = "ls -al a*";
    // char *next_ptr;
    char *sArr[100] = {
        NULL,
    };
    function(command, sArr);

    // char *str;
    // int j = 0;
    // command 의 갯수와 , 그를 담는 문자열 배열

    // for (j = 0, str = command;; str = NULL, j++)
    // {
    //     sArr[j] = strtok_r(str, " ", &next_ptr);
    //     if (sArr[j] == NULL)
    //         break;
    // }
    // for (int i = 0; i < 10; i++)
    // {
    //     if (sArr[i] != NULL)
    //         printf("%s\n", sArr[i]);
    // }
}