#include <stdio.h>
#include <mpi.h>


float avg(int *x, int M)
{
	float ans = 0.0;
	for(int i = 0; i < M; i++)
		ans = ans+x[i];
	return ans/M;
}

void main(int argc, char* argv[])
{
	int rank,size;
	float c;
	int N;
	int M;
	
	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);

	if(rank == 0)
	{
		N=size;
		printf("Enter value of M: ");
		scanf("%d", &M);
	}

	MPI_Bcast(&M, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int b[M];
	float x[N];

	int a[N*M];

	if(rank == 0)
	{	
		printf("Enter %d values: ", N*M);
		for(int i=0; i<N*M; i++)
		{
			scanf("%d", &a[i]);
		}

	}

	MPI_Scatter(a, M, MPI_INT, b, M, MPI_INT, 0, MPI_COMM_WORLD);

	c = avg(b, M);

	printf("value of average in rank %d : %f \n", rank, c);

	MPI_Gather(&c, 1, MPI_FLOAT, x, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

	if(rank == 0)
	{
		float ans = 0.0;
		for(int i = 0; i < N; i++)
			ans = ans+x[i];
		ans = ans/N;
		printf("\nFinal Avg = %f \n", ans);
	}

	MPI_Finalize();



}
