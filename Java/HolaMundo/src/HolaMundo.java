
import java.util.Scanner;

//Nuestro primer programa HolaMundo
/*
Para escribir varias lineas.
 */
public class HolaMundo {

    public static void main(String[] args) {
        /*  System.out.println("Hola mundo");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);*/

        // Var - inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        //soutv + tab
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //Para ejecutar Shift + F6 
        //Reglas para defeinir una variable en Java
        var usuario ="Osvaldo";   //video 2.5
        var titulo = "Ingeniero";
        var union = titulo +" "+ usuario;
        System.out.println("union = " + union);
        var a = 8;
        var b = 4;
        System.out.println( usuario + a + b);*/
        //Ejercicio con Caracteres Especiales con Java
//        var nombre = "Natalia";
//        System.out.println("Nueva linea: \n" + nombre);// Diagonal inversa y letra n hacen el salto de linea
//        System.out.println("Tabulador: \t" + nombre); //Tabulador un espacio para centrar
//        System.out.println("\t\t.:MENÚ:.");
//        System.out.println("Retroseso: \b\b"+nombre);//Caracter de retroseso
//        System.out.println("Comillas simples: \'"+nombre+"\'");
//        System.out.println("Comillas Dobles: \""+nombre+"\"");
//        //Clase Scanner
//        Scanner entrada = new Scanner(System.in);
//        System.out.println("Digite su nombre: ");
//        var usuario2 = entrada.nextLine();
//        System.out.println("usuario2 0 " + usuario2);
//        System.out.println("Escriba el título: ");
//        var titulo2 = entrada.nextLine();
//        System.out.println("Resultado: "+titulo2+" "+usuario2);
//        
//        byte numEnteroByte = 127;
//        System.out.println("numEnteroByte = " + numEnteroByte);
//        System.out.println("Valor minimo del byte:"+ Byte.MIN_VALUE);
//        System.out.println("Valor máximo del byte:"+ Byte.MAX_VALUE);
//        
//        short numEnteroShort = 32767;
//        System.out.println("numEnteroShort = "+ numEnteroShort);
//        System.out.println("Valor minimo del short: "+ Short.MIN_VALUE);
//        System.out.println("Valor máximo del short: "+ Short.MAX_VALUE);
//        
//        int numEnteroInt = 2147483647;
//        System.out.println("numEnteroInt = " + numEnteroInt);
//        System.out.println("Valor mínimo del int: " + Integer.MIN_VALUE);
//        System.out.println("Valor máximo del int: " + Integer.MAX_VALUE);
//        
//        long numEnteroLong = 9223372036854775807L;
//        System.out.println("numEnteroLong = " + numEnteroLong);
//        System.out.println("Valor mínimo long: "+Long.MIN_VALUE);
//        System.out.println("Valor máximo long: "+Long.MAX_VALUE);
//        
//        float numFloat = 3.4028235E38F;
//        System.out.println("numFloat = "+numFloat);
//        System.out.println("El valor minimo de float: "+Float.MIN_VALUE);
//        System.out.println("El valor máximo de float: "+Float.MAX_VALUE);
//        
//        double numDouble = 1.7976931348623157E308D;
//        System.out.println("numDouble = " + numDouble);
//        System.out.println("El valor mínimo de double: " + Double.MIN_VALUE);
//        System.out.println("El valor máximo de double: " + Double.MAX_VALUE);
//        
//        //Inferencia de tipos var y tipos primitivos
//        var numEntero = 20; //Las literales sin punto automaticamente son int
//        System.out.println("numEntero = " + numEntero);
//       // var numFloat = 10.0F; //Automaticamente con el punto se transforma el tipo double
//        System.out.println("numFloat = " + numFloat);
//       // var numDouble = 10.0;
//        System.out.println("numDouble = " + numDouble);
//        
//        //Tipos primitivos char
//        char miVariableChar = 'a';
//        System.out.println("miVariableChar = " + miVariableChar);
//        
//        char varCaracter = '\u0024'; // Indicamos a Java la signación con el código unicode
//        System.out.println("varCaracter = " + varCaracter);
//        char varCaracterDecimal = 36; // Valor decimal del juego de caracteres unicode
//        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
//        char varCaracterSimbolo = '$'; // UN caracter especial, podemos copiar y pegar desde unicode
//        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
//        
//        var varCaracter1 = '\u0024'; // Indicamos a Java la signación con el código unicode
//        System.out.println("varCaracter1 = " + varCaracter1);
//        var varCaracterDecimal1 = (char)36; 
//        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
//        var varCaracterSimbolo1 = '$'; // UN caracter especial, podemos copiar y pegar desde unicode
//        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
//        
//        int varEnteroChar = '$';
//        System.out.println("varEnteroChar = " + varEnteroChar);
//        int caracterChar = 'b';
//        System.out.println("caracterChar = " + caracterChar);
//        
//        //Tipos primitivos tipos booleanos
//        var varBool = false;
//        System.out.println("varBool = " + varBool);
//        
//        if(varBool){
//            System.out.println("La bandera es verde");
//        }
//        else {
//            System.out.println("La bandera es roja");
//        }
//        
//        //Algoritmo: ¿Es mayor de edad?
//        var edad = 15; // Literal tener presente la inferencia de tipos
//        //var adulto = edad >=18; // Es la expresión booleana
//        if (edad >= 18){
//            System.out.println("Eres mayor de edad");
//        }
//        else{
//            System.out.println("Eres menor de edad");
//        }
//        //Conversión de tipos primitivos
//        //var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//        var valorPI = Double.parseDouble("3.1416");
//        System.out.println("valorPI = " + valorPI);
//        
//        //Pedir un valor
//        //var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad: ");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad); 
//        
//        //Conversión de tipos primitivos en java Parte 2
//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//        
//        var fraseChar = "programadores".charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//        //var entrada = new Scanner(System.in);
//        System.out.println("Digite un caracter: ");
//        fraseChar = entrada.nextLine().charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
    }
}
