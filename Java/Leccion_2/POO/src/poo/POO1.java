
package poo;


public class POO1 {

   
    public static void main(String[] args) {
        
       Persona persona = new Persona(); //LLamamos al constructor
       Persona persona1 = new Persona(); //LLamamos al constructor
       
       
       persona.nombre = "Juan";
       persona.apellido = "Goméz";       
       persona.obtenerInformacion(); //Llamamos al método
       persona1.nombre = "Horacio";
       persona1.apellido = "Cortez";       
       persona1.obtenerInformacion(); //Llamamos al método 
       
       
     
        
       
    }
    
}
