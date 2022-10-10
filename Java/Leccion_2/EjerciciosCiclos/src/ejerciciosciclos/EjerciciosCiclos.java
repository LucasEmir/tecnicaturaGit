package ejerciciosciclos;

import java.util.Scanner;

public class EjerciciosCiclos {

    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);
        int numero;
                
        do {

            System.out.println("Ingresar un número positivo.");
            numero = leer.nextInt();
            if (numero > 0) {
                int cuadrado = numero * numero;
                System.out.println("El cuadrado del número ingresado es: " + cuadrado);
            } else {
                System.out.println("El número ingresado no es positivo.");
            }
        } while (numero >= 0);
    }

}
