/*1)Programa una función que cuente el 
número de caracteres de una cadena de 
texto.
*/

const numCadena = (cadena = "") =>{
    return cadena.length;
  }
  


/*2) Programa una función que te devuelva el texto recortado según el número de caracteres indicados, 
pe. miFuncion("Hola Mundo", 4) devolverá "Hola".*/

const recortar = (cadena,numCaracteres) =>{
  if (typeof(cadena) === 'object'){
    return undefined;
  }else{
  return cadena.slice(0,numCaracteres);
  }
}
/*
3) Programa una función que dada una String te devuelva un Array de textos separados por cierto caracter,
 pe. miFuncion('hola que tal', ' ') devolverá ['hola', 'que', 'tal'].*/

 const sepCaracter = (cadena = " ",separador = " ") =>{

  if (cadena == " " && separador ==  " "){
    return null;
  }else if(typeof(cadena) === 'string'){
    return cadena.split(separador)
  }else{
    return undefined
  }
  
    
}

 /*
4) Programa una función que repita un texto X veces, 
pe. miFuncion('Hola Mundo',3) devolverá Hola Mundo Hola Mundo Hola Mundo.*/

const repet = (cadena,n) =>{

  for (let i = 0 ; i < n; i++){
      console.info(`${cadena}, ${i}`);
  }

}


// 5) Programa una función que invierta las palabras de una cadena de texto,
//  pe. miFuncion("Hola Mundo") devolverá "odnuM aloH".

const inverse = (cadena = null) =>{

  if (typeof(cadena) === 'string'){
    return cadena.split("").reverse().join("");
  }else if(cadena == null){
    return null
  }else{
    return undefined
  }
}

//24) Programa una función que dado un arreglo de números devuelva un objeto con dos arreglos, 
// el primero tendrá los numeros ordenados en forma ascendente y el segundo de forma descendiente,
//  pe. miFuncion([7,5,7,8,6]) devolverá { asc: [5,6,7,7,8], desc: [8,7,7,6,5] }.

const ascDesc = (arr) =>{

  const orden  = {
    asc: arr.map(el => el).sort(),
    des: arr.map(el => el).sort().reverse()
  }
  
  return orden;

}
// 25) Programa una función que dado un arreglo de elementos, elimine los duplicados,
//  pe. miFuncion(["x", 10, "x", 2, "10", 10, true, true]) devolverá ["x", 10, 2, "10", true].

//my way


const duplicado = (data)=>{

  let uniqueArr = [];
  data.forEach((item)=>{
    //pushes only unique element
      if(!uniqueArr.includes(item)){
      uniqueArr.push(item);
    }
  })
  return uniqueArr;
}



// 26) Programa una función que dado un arreglo de números obtenga el promedio,
//  pe. promedio([9,8,7,6,5,4,3,2,1,0]) devolverá 4.5.


const promedio = (data) =>{
  
  let sumatoria = 0;
  let promedio;

  data.forEach(element => {
      sumatoria += element; 
  });

  promedio = sumatoria/data.length;

  return promedio;
}

//Exportación de Módulos

module.exports = {numCadena, recortar , sepCaracter, inverse};