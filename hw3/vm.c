#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "page.h"

int PMem[REM_SPACE];
int PDisk[DISK_SPACE];
int PDisk_sptr = 0;

// assum Pmem is infinite

void init_pmem()
{
    int i;
    for (i = 0; i < 0x100000; i++)
    {
        PMem[i] = i + 0x10000;
    }
}
// 메모리로 복귀
int swap_in()
{
    // 메모리의 정보는 disk 에 저장 되어 있다.
    // free page 가 있어 ?
    // 없다면 하나 free page를 만들고 -> swap out
    // 있다면 disk정보를 가져와서 메모리에 올려 | 그리고 테이블 정보를 수정해.
    return 0;
}
int sawp_out()
{
    // 메모리 정보를 정리해서,
    // disk에 저장하고
    // table의 가르킴을 disk로 하고 | talbe의 상태를 바꾼다. ( 나는 disk다. )

    return 0;
}
int sawpping()
{
    return 0;
}
// like  - MMU
int access_pa(int pid, int va)
{
    // va => # , offset
    int page_n = (0xfffff000 & va) >> 12;
    int offset = 0x00000fff & va;

    // printf("va : %08x page_n : %08x|%d offset : %08x Table: %d\n", va, page_n, page_n, offset, pg_table[pid][page_n]);
    //  pg_table | 매핑  있으면 pfn , 없으면 새롭게
    if (pg_table[pid][page_n] != -1)
    {
        page_frame[page_fn].occur += 1;
        int page_fn = pg_table[pid][page_n] << 12;
        return page_fn | offset;
    }
    // freepfn 을 하나 가져와
    struct frame *res = get_free_frame();
    if (res == NULL)
    {
        printf("ERROR: No free page\n");
        exit(-1);
        return 0;
    }
    res->occur += 1;
    pg_table[pid][page_n] = res->pfn;
    int page_fn = pg_table[pid][page_n] << 12;
    printf("fault!❌ freepfn: 0x%x pgn: 0x%x pid: %d \n", res->pfn, page_n, pid);
    return page_fn | offset;
}

void main(int argc, char *argv[])
{
    char *input_file_name = "input_vm";
    ;
    FILE *fp; //input file ptr
    char *line = NULL;
    char *saveptr;

    char *pid_str;
    char *va_str;
    char *rw_str;
    int pid;
    int va;
    int pa;
    int rw;
    char *e;

    int pg;
    int pg_offset;
    size_t len;

    if (argc == 2)
    {
        input_file_name = argv[1];
    }
    fp = fopen(input_file_name, "r");

    page_init();
    init_pmem();

    // get a line from input
    while (getline(&line, &len, fp) != -1)
    {
        pid_str = strtok_r(line, " \n", &saveptr);
        va_str = strtok_r(NULL, " \n", &saveptr);
        // rw_str = strtok_r(NULL, " \n", &saveptr);

        pid = strtol(pid_str, &e, 16);
        va = strtol(va_str, &e, 16);
        pa = access_pa(pid, va); // needs to be translated from va
        printf("pid: %d, va: 0x%08x pa: [0x%08x] = 0x%08X ✔\n", pid, va, pa, PMem[pa]);
    }
    // print2D_(8, pg_table);
    // printf("     Pgn | Pgfn     \n");
    // for (int i = 0; i < PG_TBL_SIZE; i++)
    // {
    //     printf(" %08x| %08x \n", i, pg_table[8][i]);
    // }

    fclose(fp);
}