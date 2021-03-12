#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
	int rank, size, len, l_v_c = 0, t_v_c = 0, *p_v_c;
    char str[100], recvStr[100];

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;

    if(rank == 0){
        printf("Enter a string of length n * %d: ", size);
        scanf("%s", str);
        len = strlen(str);

        if(len%size != 0){
            printf("Invalid string.\n");
            MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
        }
    }

    MPI_Bcast(&len, 1, MPI_INT, 0, MPI_COMM_WORLD);

    MPI_Scatter(str, len/size, MPI_CHAR, recvStr, len/size, MPI_CHAR, 0, MPI_COMM_WORLD);

    for(int i = 0; i < len/size; i++){
        char ch = recvStr[i];
        if(ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' && 
            ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U') {
            l_v_c++;
        }
    }
    
    fprintf(stdout, "Rank %d:\t non-vowels count = %d\n", rank, l_v_c);
    fflush(stdout);

    p_v_c = (int*)malloc(size*sizeof(int));
    MPI_Gather(&l_v_c, 1, MPI_INT, p_v_c, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if(rank == 0){
        for(int i = 0; i < size; i++){
            t_v_c += p_v_c[i];
        }
        fprintf(stdout, "Rank %d:\t total non-vowels = %d\n", rank, t_v_c);
        fflush(stdout);
    }
    MPI_Finalize();
    return 0;
}