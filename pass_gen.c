#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int ale();
int alecm();
int alec1();

int main(){
    char esc1[2] = "";
    char esc2[2] = "";
    int esc3 = 0;
    int i;
    printf("----bem vindo ao gerador de senha----\n");
    printf("----sua senha deve conter caracteres especiais?[y][n]: \n");
    scanf("%s", esc1);
    printf("----sua senha deve conter números?[y][n]: ");
    scanf("%s", esc2);
    printf("----quantos digitos deve ter a senha?: \n");
    scanf("%d", esc3);
    
    
}

int ale(esc0){
    char resu[] = "";
    int aleator = 10;
    for (int i = 0; i<= esc0; i++){
        int random = rand() % (aleator);
        resu[i] = random;
    }
    return resu;
}

int alecm(escoi){
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

int alec1(esco){
    int escoi = rand()% 2+1;
    char resul[50] = "";
    int alea = 26;
    for (int i =0; i<= esco; i++){
        resul[i] = escoi;
    }
    return resul;
}