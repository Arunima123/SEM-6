#include "mpi.h"
#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[])
{
	int rank;
	char str[5]="HeLLO";
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);

	if(rank< strlen(str))
	{
		if(str[rank]>='A' && str[rank]<='Z')
			str[rank]+=32;
		else if(str[rank]>='a' && str[rank]<='z')
			str[rank]-=32;

		printf("%c, Rank: %d\n",str[rank],rank);
	}

	

	MPI_Finalize();
	return 0;
}	

