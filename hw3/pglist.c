#include <stdio.h>
#include <string.h>
#include "page.h"

static struct frame *free_list;
// free frame list
struct frame *get_free_frame()
{
    if (free_list->n == NULL)
    {
        return NULL;
    }
    // free_list 에서 첫번째거를 가져와서 반환한다.
    struct frame *res = free_list;
    // free_list에서는 제명
    free_list = free_list->n;
    return res;
}
struct frame *restore_free_frame(struct frame *restore)
{
    restore->n = free_list;
    free_list->p = restore;
    free_list = restore;

    return free_list;
}
struct frame *find_evict_frame()
{
    int frameIdx = -1;
    int min_val = -1;
    for (int i = 0; i < MAX_FRAMES; i++)
    {
        if (min_val == -1 || min_val < page_frame[i].occur)
        {
            frameIdx = i;
            min_val = page_frame[i].occur;
        }
    }
    printf("less frame is %d \n", frameIdx);

    return page_frame[frameIdx];
}

void page_init()
{
    struct frame *p;
    struct frame *n;

    // initialize pg_frames
    memset(page_frame, 0, sizeof(page_frame));
    // initialize pg_table by -1 : -1 : no connection

    for (int i = 0; i < NPROC; i++)
    {
        for (int j = 0; j < PG_TBL_SIZE; j++)
        {
            pg_table[i][j] = -1;
        }
    }

    for (int i = 0; i < MAX_FRAMES; i++)
    {
        // fill in free page frames list
        page_frame[i].pfn = i;
        if (i > 0)
            page_frame[i].p = &page_frame[i - 1];

        if (i < MAX_FRAMES - 1)
            page_frame[i].n = &page_frame[i + 1];
    }
    free_list = &page_frame[0];
}
// DEBUG - utils

void print2D_(int pid, int arr[][PG_TBL_SIZE])
{

    for (int j = 0; j < PG_TBL_SIZE; j++)
    {
        printf("%d ", pg_table[pid][j]);
    }
    printf("\n");
}
void print2D(int arr[][PG_TBL_SIZE])
{
    for (int i = 0; i < NPROC; i++)
    {
        for (int j = 0; j < PG_TBL_SIZE; j++)
        {
            printf("%d ", pg_table[i][j]);
        }
        printf("\n");
    }

    printf("\n");
}