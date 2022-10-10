package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclos02 {

    public static void main(String[] args) {

        var numero = Integer.parseInt(JOptionPane.showInputDialog("Por favor digite un número."));
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El número " + numero + " es POSITIVO.");
            } else {
                System.out.println("El número " + numero + " es NEGATIVO.");
            }

            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número."));

        }
        System.out.println("El número " + numero + " finaliza el programa.");

    }

}
