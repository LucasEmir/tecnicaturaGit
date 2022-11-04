var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Betancud';
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izquierda a derecha siguiendo la cadena lee el número como str
console.log(juntos);
juntos = nombre + 78 + 17; //Si le colocamos paréntesis los suma por ej (78+17) nos daría 95.
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera concatenación usando operador simplificado
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const
let nombre2 = 'Pedro';
console.log(nombre2);

const apellido2 = 'Lepes';
//apellido2 = 'Perez'; es una constante, no puede ser modificada
console.log(apellido2);

let x, y; //Se puede crear varias variables dentro de una misma línea
x = 17, y =21; //Se puede hacer asignación de varias variables dentro de la misma línea
let z = x + y; //Se asigna el valor de la operación
console.log(z);

let _1num = 31; //No utilizar números para inicializar variables
let rompiendo = 'rompe';//No utilizar palabras reservadas para variables ej. break

console.log(_1num);
console.log(rompiendo);
