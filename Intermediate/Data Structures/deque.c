/*
Author: dvlpsh
Description: demonstration of a double ended queue using arrays in C
*/
//deque implementation using array.

#include<stdio.h>
#include<stdlib.h>

#define item int

typedef struct
{
	item *a;
	int r,f,size;
}Q;

void init(Q *q, int n);
int isEmpty(Q *q);
int isFull(Q *q);
int EnqueueRear(Q *q, item z);
item DequeueFront(Q*q);
item front(Q *q);
item rear(Q *q);
item DequeueRear(Q *q);
int EnqueueFront(Q *q, item z);

int main()
{
	Q q;
	int n, ch,res, num;
	printf("Enter the size of Queue.\n");
	scanf("%d", &n);
	init(&q,n);
	
	
	do
	{
		//menu
		printf("\nMenu:\n1.EnqueueRear\n2.DequeueFront\n3.EnqueueFront\n4.DequeueRear\n5.PeekFront\n6.PeekRear\n7.-1 to exit\n\n");
		scanf("%d", &ch);
	
		switch(ch)
		{
			case 1:
				printf("Enter item to EnqueueRear.\n");
				scanf("%d", &num);
				if(EnqueueRear(&q, num) == 0)//Successfully Enqueued
					printf("Successfully Enqueued in the Rear.\n");
				else
					printf("Queue is full Cannot add any more elements.\n");
				break;
				
			case 2:
				if(!isEmpty(&q))
					printf("Item Dequeued from Front is: %d\n", DequeueFront(&q));
				else //if(front(&q) == -1)
					printf("Queue Empty\n");
				break;
				
			case 3:
				printf("Enter item to EnqueueFront.\n");
				scanf("%d", &num);
				if(EnqueueFront(&q, num) == 0)//Successfully Enqueued
					printf("Successfully Enqueued in Front.\n");
				else 
					printf("Queue is full Cannot add any more elements.\n");
				break;
				
			case 4:
				if(!isEmpty(&q))
					printf("Item Dequeued from Rear is: %d.", DequeueRear(&q));
				else //if(front(&q) == -1)
					printf("Queue Empty\n");
				break;
				
			case 5:
				if(front(&q) != -1)
				printf("PeekFront element is %d.", front(&q));
				else
				printf("Queue Empty.");
				break;
				
			case 6:
				if(rear(&q) != -1)
				printf("PeekFront element is %d.", rear(&q));
				else
				printf("Queue Empty.");
				break;
			

		}
	}
	while(ch!=-1);
	
	
	printf("Exiting.\n");
	return 0; //Exit
}


int isFull(Q *q)
{
	if(((q->f == 0) && (q->r == q->size-1) )|| (q->f == q->r+1))
		return 1;
	
	else 
		return 0; //false
}


int EnqueueRear(Q *q, item z)
{
	if(isFull(q))
	{
		//printf("Queue is full. Cannot enter elements");
		return -1; //Queue is full
	}

	else
	{
		if(q->r == q->size-1) //All spaces filled except position 0
			q->r = -1;
		if(q->f == -1) //if queue is empty
			q->f = 0;
			
		q->a[++q->r] =z;

		return 0; //successfull
	}

}


int isEmpty(Q *q)
{
	if((q->r == -1) || (q->f == -1))
		return 1; //Empty
	else 
		return 0; //not Empty
}


item DequeueFront(Q *q)
{
	item z;
	if(isEmpty(q))
		return -1; //Queue Empty so cannot dequeue
	else
	{
		z = q->a[q->f];
		//q->a[q->f] = -1;
		if(q->r == q->f)
		{
			q->r = -1;
			q->f = -1;
		}

		else if(q->f == q->size-1)
			q->f = 0;
			
		else
			q->f++;
			
		
		return z;

	}
}


item front(Q *q)
{
	if(q->f == -1 && q->r ==-1)
		return -1;
	else
		return q->a[q->f];
}


void init(Q *q, int n)
{
	q->size = n;
	q->r = -1;
	q->f = -1;
	q->a = (item *)malloc(q->size *(sizeof(int)));
}


item DequeueRear(Q *q)
{
	item z;

	if(isEmpty(q))
		return -1; //isEmpty
		
	z = q->a[q->r];
	//q->a[q->r]=-1;
	if(q->r == q->f)
	{
		q->r = -1;
		q->f = -1;
	}

	else if(q->r == 0)
		q->r = q->size-1;
		
	else
	
		q->r--;
		
		
	return z;

}


int EnqueueFront(Q *q, item z)
{
	if(isFull(q))
		return -1; //Queue is full and cannot Enqueue

	else
	{
		if(q->f == -1) //Queue Empty
		{
			q->f = q->size-1;
			q->r = q->size-1;
		}
		
		else if(q->f == 0)
			q->f = q->size-1;
		
		else 
			q->f--;
			
			
		q->a[q->f] = z;
		
		return 0; //Successfull
		
	}
}

item rear(Q *q)
{

	if(q->f == -1 && q->r ==-1)
		return -1;
	else
		return q->a[q->r];
}

