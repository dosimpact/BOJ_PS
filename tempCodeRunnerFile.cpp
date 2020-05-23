#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct node
{
    int data;
    struct node *right; //오른쪽 자식노드의 주소
    struct node *left;  // 왼쪽 자식노드의 주소
} NODE;

NODE *root = NULL;

NODE *init(int data)
{

    NODE *tmp = (NODE *)malloc(sizeof(NODE));
    memset(tmp, NULL, sizeof(NODE));
    tmp->data = data;
    return tmp;
}

void add(int data, NODE **addr)
{

    NODE *tmp = *addr;

    //공석이면 노드 대입 -> 함수 종료

    if (!tmp)
    {
        *addr = init(data);
        printf("%d저장완료\n", data);
    }

    //data가 작을 경우 -> 왼쪽 자식으로
    else if (data < tmp->data)
    {
        add(data, &tmp->left);
    }
    //data가 클 경우 -> 오른쪽 자식으로
    else if (data > tmp->data)
    {
        add(data, &tmp->right);
    }
    else
    {
        printf("중복 원소는 저장할 수 없습니다. \n");
    }

    //data가 같을 경우 -> 저장x, 함수종료
}

void preorder(NODE *tmp) //전위 순회
{
    if (!tmp)
    {
        return;
    }
    printf("%d", tmp->data);
    preorder(tmp->left);
    preorder(tmp->right);
}

void inorder(NODE *tmp) //중위 순회
{
    if (!tmp)
    {
        return;
    }
    inorder(tmp->left);
    printf("%d", tmp->data);
    inorder(tmp->right);
}

void postorder(NODE *tmp) //후위 순회
{
    if (!tmp)
    {
        return;
    }
    postorder(tmp->left);
    postorder(tmp->right);
    printf("%d", tmp->data);
}

int main()
{
    add(100, &root);
    add(150, &root);
    add(50, &root);
    add(75, &root);
    add(200, &root);
    add(125, &root);
    add(35, &root);
    add(75, &root);
    add(80, &root);

    printf("전위 : ");
    preorder(root);
    printf("\n");

    printf("중위 : ");
    inorder(root);
    printf("\n");

    printf("후위 : ");
    postorder(root);
    printf("\n");

    return 0;
}