def suma(x: float ,y : float) -> float:
    
    """Funcion que genera toma 2 argumentos y devuelve una suma 
    
    args:
        x:(float): primer valor a sumar 
        y:(float): segundo valor a sumar 
    """
    return x+y


def escribir(fpath,data_in):
    """Funcion que escribe en un archivo

    Args:
        fpath (String): Path Absoluto del archivo
        data_in (String): Informacion a Escribir
    """
    
    with open(fpath,"w") as file_in :
        file_in.write(data_in)
        
        
        
class calculadora:
    """
    Clase Calculadora
    """
    def multiplicacion(x,y):
        """
        Funcion que toma 2 argumentos y devuelve la multiplicacion 

        Args:
            x (int/float): Primer argumento a multiplicar
            y ([type]): 
        """
        return x*y
    