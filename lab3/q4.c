#include <stdio.h>
#include "mpi.h"
#include <string.h>
int main(int argc, char *argv[])
{
    MPI_Init(&argc,&argv);
    int rank,size;
    MPI_Status status;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    int m;
    char s1[100],c1[100],s2[100],c2[100],l[200],ans[200];
    if(rank==0){
        fprintf(stdout, "Enter a string of length %d*n: ", size);
        fflush(stdout);
        scanf("%s",s1);
        fprintf(stdout, "Enter a string of length %u: ", strlen(s1));
        fflush(stdout);
        scanf("%s",s2);
        m=strlen(s1)/size;
    }
    MPI_Bcast(&m,1,MPI_INT,0,MPI_COMM_WORLD);
    MPI_Scatter(s1,m,MPI_CHAR,c1,m,MPI_CHAR,0,MPI_COMM_WORLD);
    MPI_Scatter(s2,m,MPI_CHAR,c2,m,MPI_CHAR,0,MPI_COMM_WORLD);

    c1[m]='\0';
    c2[m]='\0';
      for(int i=0;i<2*m;i+=2){
        l[i]=c1[i/2];
        l[i+1]=c2[i/2];
    }
    l[2*m]='\0';
    fprintf(stdout, "Recieved '%s' and '%s' by Rank %d\n",c1,c2,rank);
    fflush(stdout);
    MPI_Gather(l,2*m,MPI_CHAR,ans,2*m,MPI_CHAR,0,MPI_COMM_WORLD);
    if(rank==0){
        fprintf(stdout, "Answer: %s in Rank %d\n",ans,rank);
        fflush(stdout);
    }
    MPI_Finalize();
    return 0;
}