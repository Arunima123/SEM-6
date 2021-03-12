#include <stdio.h>
#include <mpi.h>

int factorial(int x)
{
	int ans = 1;
	for(int i = x; i > 0; i--)
		ans = ans*i;
	return ans;
}

void main(int argc, char* argv[])
{
	int rank,size, c;
	int N;
	int sum=0;
	int a[N], b[N];

	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);

	if(rank == 0)
	{
		N=size;		
		printf("Enter %d values: ",N);
		for(int i=0; i<N; i++)
		{
			scanf("%d", &a[i]);
		}
	}

	MPI_Scatter(a, 1, MPI_INT, &c, 1, MPI_INT, 0, MPI_COMM_WORLD);

	c = factorial(c);

	MPI_Gather(&c, 1, MPI_INT, b, 1, MPI_INT, 0, MPI_COMM_WORLD);

	if(rank == 0)
	{
		for(int i=0; i<N; i++)
		{
			printf("Root recieved %d from process %d \n", b[i], i);
			sum+=b[i];
		}
	printf("The sum of all the factorials: %d",sum);
	}

	MPI_Finalize();

}