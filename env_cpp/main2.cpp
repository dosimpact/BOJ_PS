#include <pthread.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define BUFFER_SIZE 1000
#define MAX_STRING_LENGTH 30
#define ASCII_SIZE 256

pthread_cond_t thread_cond_producer = PTHREAD_COND_INITIALIZER;
pthread_cond_t thread_cond_consumer = PTHREAD_COND_INITIALIZER;

typedef struct sharedobject
{
    FILE *rfile;
    int linenum;
    char *lineQ[BUFFER_SIZE]; // stack Buffer
    int Sidx;                 // stack buffer idxer can READ [0,100)
    pthread_mutex_t lock;
    int fin; // fin = 0 > 1 end read file
    //int alphas['z' - 'a' + 1];
    int stat[MAX_STRING_LENGTH];
    int stat2[ASCII_SIZE];
} so_t;

void printAZ(int *stat2)
{
    printf("       A        B        C        D        E        F        G        H        I        J        K        L        M        N        O        P        Q        R        S        T        U        V        W        X        Y        Z\n");
    printf("%8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d %8d\n",
           stat2['A'] + stat2['a'], stat2['B'] + stat2['b'], stat2['C'] + stat2['c'], stat2['D'] + stat2['d'], stat2['E'] + stat2['e'],
           stat2['F'] + stat2['f'], stat2['G'] + stat2['g'], stat2['H'] + stat2['h'], stat2['I'] + stat2['i'], stat2['J'] + stat2['j'],
           stat2['K'] + stat2['k'], stat2['L'] + stat2['l'], stat2['M'] + stat2['m'], stat2['N'] + stat2['n'], stat2['O'] + stat2['o'],
           stat2['P'] + stat2['p'], stat2['Q'] + stat2['q'], stat2['R'] + stat2['r'], stat2['S'] + stat2['s'], stat2['T'] + stat2['t'],
           stat2['U'] + stat2['u'], stat2['V'] + stat2['v'], stat2['W'] + stat2['w'], stat2['X'] + stat2['x'], stat2['Y'] + stat2['y'],
           stat2['Z'] + stat2['z']);
}
void *producer(void *arg)
{

    so_t *so = arg;
    int *ret = malloc(sizeof(int));
    FILE *rfile = so->rfile;
    int i = 0;
    char *line = NULL;
    size_t len = 0;
    ssize_t read = 0;
    //------------------------------------------init setting
    pthread_mutex_lock(&so->lock);
    while (1)
    {
        //데이터를 더 채울 수 있는 경우  // Read More Case
        if (so->Sidx < BUFFER_SIZE && so->fin == 0)
        {
            read = getdelim(&line, &len, '\n', rfile);
            if (read == -1)
            {
                printf("producer : READING complete! \n");
                so->fin = 1;
                //pthread_cond_broadcast(&thread_cond_producer);
                pthread_cond_broadcast(&thread_cond_consumer);
                break;
            }
            if (so->Sidx == -1)
            {
                so->Sidx = 0;
            }
            so->linenum = i;
            so->lineQ[so->Sidx] = strdup(line); /* share the line */
            printf("line : %d is upload complete\n", so->linenum);
            i++;
            so->Sidx++;
            pthread_cond_broadcast(&thread_cond_consumer);
        }
        else if (so->Sidx >= BUFFER_SIZE && so->fin == 0)
        { //데이터가 소비가 안된경우 //Sleep Case
            printf("producer sleep\n");
            pthread_cond_wait(&thread_cond_producer, &so->lock);
            pthread_cond_broadcast(&thread_cond_consumer);
        }
        else if (so->fin == 1)
        { //데이터를 다 읽은 경우 //End case
            //pthread_cond_broadcast(&thread_cond_producer); // when multi producer, wake up others!
            pthread_cond_broadcast(&thread_cond_consumer);
        }
        else
        {
            printf("ERROR!\n");
        }
    }
    pthread_mutex_unlock(&so->lock);
    free(line);
    printf("Prod_%x: %d lines\n", (unsigned int)pthread_self(), i);
    *ret = i;
    pthread_exit(ret);
}

void *consumer(void *arg)
{
    so_t *so = arg;
    int *ret = malloc(sizeof(int));
    int i = 0;
    int len;
    char *line = NULL;
    //------------------------------------------init setting
    //int alphas['z' - 'a' + 1];
    size_t length = 0;
    int stat[MAX_STRING_LENGTH];
    int stat2[ASCII_SIZE];
    memset(stat, 0, sizeof(stat));
    memset(stat2, 0, sizeof(stat));
    pthread_mutex_lock(&so->lock);
    while (1)
    {
        // 데이터를 더 읽을 수 있는 경우// Consume Case || 다 읽으면 자버리기 Sidx -1, 100
        if ((0 <= so->Sidx && so->Sidx <= BUFFER_SIZE))
        {
            so->Sidx--;
            if (so->Sidx <= -1)
            {
                continue;
            }
            line = so->lineQ[so->Sidx];
            so->lineQ[so->Sidx] = NULL;
            len = strlen(line);
            printf("Cons_%x: [%02d:%02d] %s",
                   (unsigned int)pthread_self(), i, so->linenum, line);
            int j = 0;
            for (j = 0; line[j]; j++)
            {
                stat2[line[j]]++;
            }
            length = strlen(line);
            if (length >= 30)
                length = 30;
            if (length <= 0)
                length = 1;
            stat[length - 1]++;
            i++;
            free(line);
            if (so->Sidx <= -1)
            {
                continue;
            }
        }
        else if (so->fin == 0 && (so->Sidx <= -1 || so->Sidx > BUFFER_SIZE)) // 끝나지 않았지만, 읽을데이터가 없는 경우 // Sleep case
        {
            printf("consumer sleep\n");
            pthread_cond_broadcast(&thread_cond_producer);
            pthread_cond_wait(&thread_cond_consumer, &so->lock);
        }
        else if (so->fin == 1) //End case
        {
            pthread_cond_broadcast(&thread_cond_consumer);
            pthread_cond_broadcast(&thread_cond_producer);
            break;
        }
    }

    printf("Cons: %d lines\n", i);
    // for (int it = 0; it < ('z' - 'a' + 1); it++)
    // {
    //     printf("[%c] : %d ", 'a' + it, alphas[it]);
    //     so->alphas[it] += alphas[it];
    // }
    // state share
    printAZ(stat2);
    for (int it = 0; it < MAX_STRING_LENGTH; it++)
    {
        so->stat[it] += stat[it];
    }
    for (int it = 0; it < ASCII_SIZE; it++)
    {
        so->stat2[it] += stat2[it];
    }
    //printf("\n");
    pthread_mutex_unlock(&so->lock);
    *ret = i;
    pthread_exit(ret);
}

int main(int argc, char *argv[])
{
    pthread_t prod[100];
    pthread_t cons[100];
    int Nprod, Ncons;
    int rc;
    long t;
    int *ret;
    int i;
    FILE *rfile;
    if (argc == 1)
    {
        printf("usage: ./prod_cons <readfile> #Producer #Consumer\n");
        exit(0);
    }
    so_t *share = malloc(sizeof(so_t));
    memset(share, 0, sizeof(so_t));
    rfile = fopen((char *)argv[1], "r");
    if (rfile == NULL)
    {
        perror("rfile");
        exit(0);
    }
    if (argv[2] != NULL)
    {
        Nprod = atoi(argv[2]);
        if (Nprod > 100)
            Nprod = 100;
        if (Nprod == 0)
            Nprod = 1;
    }
    else
        Nprod = 1;
    if (argv[3] != NULL)
    {
        Ncons = atoi(argv[3]);
        if (Ncons > 100)
            Ncons = 100;
        if (Ncons == 0)
            Ncons = 1;
    }
    else
        Ncons = 1;

    share->rfile = rfile;
    share->Sidx = -1;
    pthread_mutex_init(&share->lock, NULL);
    for (i = 0; i < Nprod; i++)
    {
        int res = pthread_create(&prod[i], NULL, producer, share);
        if (res < 0)
        {
            perror("thread create error");
        }
    }
    usleep(10);
    for (i = 0; i < Ncons; i++)
    {
        int res = pthread_create(&cons[i], NULL, consumer, share);
        if (res < 0)
        {
            perror("thread create error");
        }
    }

    printf("main continuing\n");

    for (i = 0; i < Ncons; i++)
    {
        rc = pthread_join(cons[i], (void **)&ret);
        printf("main: consumer_%d joined with %d\n", i, *ret);
    }
    for (i = 0; i < Nprod; i++)
    {
        rc = pthread_join(prod[i], (void **)&ret);
        printf("main: producer_%d joined with %d\n", i, *ret);
    }
    printf("-------------- final A-Z counter ---------------\n");
    // for (int it = 0; it < ('z' - 'a' + 1); it++)
    // {
    //     printf("[%c] : %d ", 'a' + it, share->alphas[it]);
    // }
    // sum
    int sum = 0;
    for (i = 0; i < 30; i++)
    {
        sum += share->stat[i];
    }
    // print out distributions
    printf("*** print out distributions *** \n");
    for (i = 0; i < 30; i++)
    {
        int j = 0;
        int num_star = share->stat[i] * 80 / sum;
        printf("[lineLen : %3d]: %4d \t", i + 1, share->stat[i]);
        for (j = 0; j < num_star; j++)
            printf("*");
        printf("\n");
    }
    printAZ(share->stat2);
    printf("\n");
    pthread_exit(NULL);
    exit(0);
}
