/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un número negativo.
*/
package Ciclos01;

import java.util.Scanner;



public class Ciclos01 {
    
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Por favor ingrese un número: ");
        numero = Integer.parseInt(leer.nextLine());
        while(numero >= 0){ //Mientras el número sea igual a 0 o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Ingresar otro número1: ");
            numero = Integer.parseInt(leer.nextLine());
        }
        
        System.out.println("El ejercicio a finalizado por ingresar un número negativo.");
    }
   
    
}
