const prompt = require('prompt-sync')()

function calcular(num1, num2, oper){
    switch (oper) {
        case "+":
            console.log(`O resultado da soma de ${num1} e ${num2} é: ${num1+num2}`)
        case "-":
            console.log(`O resultado da subtração de ${num1} e ${num2} é: ${num1-num2}`)
        case "*":
            console.log(`O resultado da multiplicação de ${num1} e ${num2} é: ${num1*num2}`)
        case "/":
            console.log(`O resultado da divisão de ${num1} e ${num2} é: ${num1/num2}`)
    }
}

var num1 = prompt('digite o primeiro valor > ')
var num2 = prompt('digite o segundo valor > ')
var operacao = prompt('digite a operacao > ')

calcular(num1, num2, operacao)