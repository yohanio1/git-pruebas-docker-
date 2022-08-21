const excercise = require('../examples');

//-------------------------------------------------------------------------------------------------------------------
describe('excercise #1',() =>{

  test('cadena Hola length =  4', () => {
    expect(excercise.numCadena("Hola")).toBe(4);
  });
  test('number is undefined',() =>{
    expect(excercise.numCadena(12)).toBeUndefined();
  });
  test('object is undefined',() =>{
    let objectTest = {
      nombre: "Juan",
      edad: 12
    };
    expect(excercise.numCadena(objectTest)).toBeUndefined();
  });
})
  
//-------------------------------------------------------------------------------------------------------------------
describe('excercise #2',() =>{

  test('slice = 4 Hola Mundo => result Hola ', () => {
    expect(excercise.recortar("Hola Mundo",4)).toBe("Hola");
  });
  test('slice = 3 Esto es una prueba => result Est ', () => {
    expect(excercise.recortar("Esto es una prueba",3)).toBe("Est");
  });
  test('slice = n empty string => result empty string ', () => {
    expect(excercise.recortar("",3)).toBe("");
  });
  test('slice = n object => result undefined ', () => {
    let objectTest = {
      nombre: "Juan",
      edad: 12
    };
    expect(excercise.recortar(objectTest,3)).toBeUndefined();
  });
})

//-------------------------------------------------------------------------------------------------------------------
describe('excercise #3',() =>{

  test('split = " " Hola como estas  => result array["Hola","como","estas"] ', () => {
    expect(excercise.sepCaracter("Hola como estas"," ")).toEqual(expect.arrayContaining(["Hola","como","estas"]));
  });

  test('no split caracter passed  any cadena  => result by default split with " " ', () => {
    expect(excercise.sepCaracter("any cadena")).toEqual(expect.arrayContaining(["any","cadena"]));
  });  
  
  test('no passed string should return undefined', () => {
    expect(excercise.sepCaracter(12)).toBeUndefined();
  });  
  
  test('no passed arguments to the function should return null', () => {
    expect(excercise.sepCaracter()).toBeNull();
  });  

})

//-------------------------------------------------------------------------------------------------------------------
describe('excercise #5',() =>{

  test('passed Hola mundo should return odnum aloH ', () => {
    expect(excercise.inverse("Hola mundo")).toBe("odnum aloH");
  });

  test('passed recononcer should return reconocer ', () => {
    expect(excercise.inverse("reconocer")).toBe("reconocer");
  });

  test('default should return null', () => {
    expect(excercise.inverse()).toBeNull();
  });

  test('passed type of no string should return undefined', () => {
    expect(excercise.inverse(12)).toBeUndefined();
  });
  
})
//-------------------------------------------------------------------------------------------------------------------
