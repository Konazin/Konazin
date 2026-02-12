#include <iostream>

using namespace std;

int Calculator(int number1, int number2, string operations){
    int result;
    if (operations == "+"){
        result = number1 + number2;
        cout << "The result is: " << result << "\n";
        exit;
    }
    else if (operations == "-"){
        result = number1 - number2;
        cout << "The result is: " << result << "\n";
        exit;
    }
    else if (operations == "x"){
        result = number1 * number2;
        cout << "The result is: " << result << "\n";
        exit;
    }
    else if (operations == "/" && number1 or number2 == 0){
        cout << "Impossible to divide by zero! \n";
        exit;
    }
    else if (operations == "/"){
        result = number1 / number2;
        cout << "The result is: " << result << "\n";
        exit;
    }
    else{
        cout << "Invalid input, ending";
        exit;
    }
    return 0;
}

int main(void){
    int number1;
    int number2;
    string operation;
    cout << "Enter firts Number: \n";
    cin >> number1;
    cout << "Enter second Number \n";
    cin >> number2;
    cout << "Enter the oparation needed ex [+][-][x][/]: \n";
    cin >> operation;
    Calculator(number1, number2, operation);
    return 0;
}