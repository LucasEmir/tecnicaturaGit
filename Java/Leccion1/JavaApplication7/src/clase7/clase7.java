
package clase7;

import java.util.Scanner;

public class clase7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
    final int salario = 1000;
    int comision = 150 , venta;
    float salarioMensual, ventaCarro, porcVenta, totalPrecio;
    
        System.out.println("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;
        
        System.out.println("\nEl salario mensual es: " + salarioMensual);
    }
}
