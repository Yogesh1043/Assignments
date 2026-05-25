#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *front = NULL;
struct node *rear = NULL;

void enqueue(int x)
{
    struct node *newnode;
    newnode = (struct node*)malloc(sizeof(struct node));

    newnode->data = x;
    newnode->next = NULL;

    if(rear == NULL)
    {
        front = rear = newnode;
    }
    else
    {
        rear->next = newnode;
        rear = newnode;
    }
}

void dequeue()
{
    if(front == NULL)
    {
        printf("Queue Underflow\n");
    }
    else
    {
        struct node *temp = front;
        printf("Deleted element: %d\n", front->data);
        front = front->next;
        free(temp);
    }
}

void display()
{
    struct node *temp = front;

    if(front == NULL)
    {
        printf("Queue is empty\n");
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
    enqueue(10);
    enqueue(20);
    enqueue(30);

    display();

    dequeue();
    display();

    return 0;
}