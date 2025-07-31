#include <stdio.h>

int main(){
    int i, j;
    char nome[30];
    printf("bote o nome que pretende reverter: \n");
    scanf("%29[^\n]s", nome);
    fflush(stdin);
    for (i=29; i!=-1; i--){
        for (j=0 ;j!=30; j++);
            nome[j] = nome[i];
    }
    printf("%s", nome);
}
