//  Tipos de Datos

//con 'var' creamos variables

/** 
// tipo: number
var edad = 20; 
console.log(edad);
console.log(typeof(edad)); //con console.log(typeof()) vemos el tipo de dato de la variable

// tipo: string
var nombre = 'alvaro';
console.log(nombre);
console.log(typeof(nombre));

// tipo: number
var sueldo = 1000.000;
console.log(sueldo);
console.log(typeof(sueldo));

// tipo: boolean
var time = false;
console.log(time);
console.log(typeof(time));

//  variable no definidad
var trabajo;
console.log(trabajo)

// variable tipo: null (vacio)
trabajo = null 
console.log(trabajo)
**/

/*** 

* Operadores matematicos +, -, *, /

*/
/** 
var edadAna, edadMaria, diferenciaEdad;
var sumaEdades, yearAna, yearMaria, yearActual;

edadAna = 32
edadMaria = 22;
yearActual = 2022


diferenciaEdad = edadAna - edadMaria;

sumaEdades = edadAna - edadMaria;

yearAna = yearActual - edadAna;
yearMaria = yearActual - edadMaria;

console.log(diferenciaEdad);
console.log(sumaEdades);
console.log('Año en que nacio Ana ' + yearAna);
console.log('Año en que nacio Ana ' + yearMaria);
console.log(yearActual * 5);
console.log(yearActual / 2);

*/

/**
 * Operadores Logicos, unarios y de asignacion
 */
// logicos <> <= >= ==
var edadAna, edadMaria, diferenciaEdad;

edadAna = 32
edadMaria = 22;


var mayorAna = edadAna > edadMaria;
console.log(mayorAna);


// Unarios, ++Incremento , --Decremento

//edadAna++;
console.log(++edadAna);
console.log(edadAna)

//Asignacion, +=, -=, *=, /=,  %=

var a = 11;
var b = 5

var c = a % 5 //Residuo a resta de una division
console.log(c);

a += b;

console.log(a)

