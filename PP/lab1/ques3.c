#include "mpi.h"
#include <stdio.h>
int main(int argc, char *argv[])
{
	int rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);

	int x=5;
	int y=6;

	if(rank==0)
		printf("Addition: %d + %d = %d\n",x,y,(x+y));
	else if(rank==1)
		printf("Subtraction: %d - %d = %d\n",x,y,(x-y));
	else if(rank==2)
		printf("Multiplication: %d * %d = %d\n",x,y,(x*y));
	else if(rank==3)
		printf("Division: %d / %d = %d\n",x,y,(x/y));

	MPI_Finalize();
	return 0;
}	
