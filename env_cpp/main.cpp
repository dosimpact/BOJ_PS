#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define BUFFER_SIZE 1000

pthread_cond_t thread_cond_producer = PTHREAD_COND_INITIALIZER;
pthread_cond_t thread_cond_consumer = PTHREAD_COND_INITIALIZER;

typedef struct sharedobject
{
	FILE *rfile;
	int linenum;
	char *lineQ[BUFFER_SIZE]; // stack Buffer
	int Sidx;				  // stack buffer idxer can READ [0,100)
	pthread_mutex_t lock;
	int fin; // fin = 0 > 1 end read file
	int alphas['z' - 'a' + 1];
} so_t;

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
	int alphas['z' - 'a' + 1];
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
				alphas[line[j] - 'a']++;
			}
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
	for (int it = 0; it < ('z' - 'a' + 1); it++)
	{
		printf("[%c] : %d ", 'a' + it, alphas[it]);
		so->alphas[it] += alphas[it];
	}
	printf("\n");
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
	printf("-------------- final a-z counter ---------------\n");
	for (int it = 0; it < ('z' - 'a' + 1); it++)
	{
		printf("[%c] : %d ", 'a' + it, share->alphas[it]);
	}
	printf("\n");
	pthread_exit(NULL);
	exit(0);
}
