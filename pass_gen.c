#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

char ale();
char alecm();
char alec1();

int main(){
    char esc1[2] = "";
    char esc2[2] = "";
    int esc3 = 0;
    char escres[4] = "";
    int i;
    printf("----bem vindo ao gerador de senha----\n");
    printf("----sua senha deve conter caracteres especiais?[y][n]: \n");
    scanf("%1s", esc1);
    printf("----sua senha deve conter números?[y][n]: ");
    scanf("%1s", esc2);
    printf("----quantos digitos deve ter a senha?: \n");
    scanf("%d", esc3);
    if(strcmp(esc1, "y")==0){
        escres[1] = 'a';
    }
    else{
        escres[1] = 'n';
    }
    if(strcmp(esc2, "y")==0){
        escres[2] = 'b';
    }
    else{
        escres[2] = 'n';
    }
}

char ale(int esc0){
    char resu[] = "";
    int aleator = 10;
    for (int i = 0; i<= esc0; i++){
        int random = rand() % (aleator);
        resu[i] = random;
    }
    return resu;
}

char alecm(int escoi){
    int escoo = rand()% 2+1;
    char ress[] = "";
    int alea = 26;
    for (int i = 0; i<= escoi; i++){
        if(escoo == 1){
            ress[i] = 'a'+ (rand()%26);
        }
        else{
            ress[i] = 'A'+ (rand()%26);
        }
    }
    return ress;
}

char alec1(int esco){
    int escoi = rand()% 2+1;
    char resul[50] = "";
    int alea = 26;
    for (int i =0; i<= esco; i++){
        resul[i] = escoi;
    }
    return resul;
}