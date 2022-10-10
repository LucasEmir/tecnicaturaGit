package CicloWhile;

public class EjercicioWhile01 {

    public static void main(String[] args) {

        var conteo = 0; //Inferencia de tipos
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }

        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);

        //Solo una línea de código nos permite omitir las llaves, pero por buenas prácticas utilizarlas.
        //for (var contador1 = 0; contador1 < 7; contador1++) 
        //System.out.println("contador1 = " + contador1);
         
        for (var contador1 = 0; contador1 < 7; contador1++) {
            if (contador1 % 2 == 0) {

                System.out.println("contador1 = " + contador1);
                break;
            }
        }

        for (var contando = 0; contando < 7; contando++) {
            
            if (contando % 2 != 0) {
                continue; //Vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
        
        }
        
        //Uso de las palabras break y continue junto a las etiquetas (labels)
        inicio:
        for (var contador2 = 0; contador2 < 7; contador2++) {

            if (contador2 % 2 != 0) {

                continue inicio;
            }
            System.out.println("contador2 = " + contador2);
        }
    }

}
