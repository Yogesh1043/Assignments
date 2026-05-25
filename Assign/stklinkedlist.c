#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *top = NULL;

void push(int x)
{
    struct node *newnode;
    newnode = (struct node*)malloc(sizeof(struct node));

    newnode->data = x;
    newnode->next = top;
    top = newnode;
}

void pop()
{
    if(top == NULL)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        struct node *temp = top;
        printf("Popped element: %d\n", top->data);
        top = top->next;
        free(temp);
    }
}

void display()
{
    struct node *temp = top;

    if(temp == NULL)
    {
        printf("Stack is empty\n");
    }
    else
    {
        while(temp != NULL)
        {
            printf("%d\n", temp->data);
            temp = temp->next;
        }
    }
}

int main()
{
    push(10);
    push(20);
    push(30);

    display();

    pop();
    display();

    return 0;
}