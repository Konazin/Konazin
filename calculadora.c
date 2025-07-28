#include <stdio.h>
#include <string.h>

int main(){
    int A, B;
    char op[6];
    printf("indique o primeiro valor: \n");
    scanf("%d", &A);
    printf("indique o segundo valor: \n");
    scanf("%d", &B);
    printf("deseja que seja qual operação das 4 principais?[sum][sub][div][mult] \n");
    scanf("%s", op);
    if (strcmp (op, "sum")==0) {
        printf("Resultado: %d", A+B);
    }
    else if(strcmp(op, "sub")==0){
        printf("Resultado: %d", A-B);
    }
    else if(strcmp(op, "div")==0){
        printf("Resultado: %d", A/B);
    }
    else if(strcmp(op, "mult")==0){
        printf("Resultado: %d", A*B);
    }
    else{
        printf("operação inválida");
    }
}