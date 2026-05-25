#include <stdio.h>

#define MAX 5

int stack[MAX];
int top = -1;

void push(int x)
{
    if(top == MAX-1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        top++;
        stack[top] = x;
    }
}

void pop()
{
    if(top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        printf("Popped element: %d\n", stack[top]);
        top--;
    }
}

void peek()
{
    if(top == -1)
    printf("Stack is empty\n");
    
    else
    printf("Top element: %d\n", stack[top]);
}

void display()
{
    if(top == -1)
    printf("Stack is empty\n");
    
    else
    {
        for(int i=top;i>=0;i--)
        printf("%d\n", stack[i]);
    }
}

int main()
{
    push(10);
    push(20);
    push(30);

    display();

    pop();
    peek();

    return 0;
}