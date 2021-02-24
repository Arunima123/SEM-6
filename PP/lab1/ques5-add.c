#include "mpi.h"
#include <stdio.h>
int main(int argc, char *argv[])
{
	int rank;
	int min;
	int max;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);

	int is_prime(int num)
	{
		int flag=0;
		for(int i=1;i<=num;i++)
			if(num%i==0)
				flag++;

		if(flag>2)
			return 0;
		else 
			return 1;
	}

	switch(rank)
	{
		case 0: min=2;
				max=50;
				break;
		case 1: min=51;
				max=100;
				break;
	}

	for(int i=min;i<=max;i++)
	{
		if(is_prime(i))
			printf("%d\n",i);
	}	

	MPI_Finalize();
	return 0;
}	