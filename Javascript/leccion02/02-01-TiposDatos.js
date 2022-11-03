// Tipos de datos en Javascript
/*
Misma sintaxis que Java
*/
// Tipo Str
var nombre = "Emir"; 
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

// Tipo númerico
var numero = 3000; 
console.log(numero);

// Tipo Objet
var objeto = {
    nombre : "Lucas",
    apellido : "Corvalán",
    telefono : "2604589555"
}
console.log(objeto);

// Tipo de dato booolean
var bandera = true;
console.log(bandera);

//Tipo de dato función (nos permite reutilizar lineas de código)
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

//Tipo de dato undefined(cualquier variable declarada pero no inicializada.)
var x ;
console.log(x);
//Tipo de dato underfined declarado 
x = undefined;
console.log(typeof x);

// null: significa ausencia de un valor
var y = null; //null no es tipo de dato, pero su origen es objet
console.log(typeof y);

//Tipo de dato de array y Empty String
var autos = ['Citroen','Audi','BMW','Ford']
console.log(autos);
console.log(typeof autos) //Los array son de tipo objet

var z = '';
console.log(z); //Esto es una cadena vacia
console.log(typeof z);