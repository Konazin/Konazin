#include <stdio.h>

int main(){
    int i, j;
    char nome[30];
    printf("bote o nome que pretende reverter: \n");
    scanf("%29[^\n]s", nome);
    for (i=29; i!=-1; i--){
        printf("%c", nome[i]);
    }
}
