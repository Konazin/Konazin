import java.util.Scanner;

public class Main{
    public static void calcular(int num1, int num2, String oper){
        var resultado = 0;
        if (oper.equals("+")){
            resultado = num1+num2;
            System.out.println("a soma é: " + resultado );
        }
        if (oper.equals("-")){
            resultado = num1-num2;
            System.out.println("a subtração é: " + resultado);
        }
        if (oper.equals("*")){
            resultado = num1*num2;
            System.out.println("A multiplicação é: " + resultado);
        }
        if (oper.equals("/")){
            resultado = num1/num2;
            System.out.println("A divisão é: " + resultado);
        }
        if (num1 == 0 || num2 == 0 && oper == "/"){
            System.out.println("Não é possível dividir por zero");
        }
        
    }
    public static void main(){
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite o primeiro valor: ");
        int num1 = entrada.nextInt();
        System.out.println("digite o segundo valor: ");
        int num2 = entrada.nextInt();
        System.out.println("digite o operador: ");
        String oper = entrada.next();
        System.out.println(oper);
        calcular(num1,num2,oper);
        entrada.close();
    }
}