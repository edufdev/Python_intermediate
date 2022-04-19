def palindrome(string):
    try: # "intento"
        if len(string) == 0: # si la longitud del string es 0
            raise ValueError ("No se puede ingresar una cadena vacia") # Elevamos un error de tipo "valueError" y le pasamos un mensaje de error
        return string == string[::1]# regresa el string si es igual a si mismo alrevez
    except ValueError as ve: # si sucede un valueError que le ponemos de nombre "ve", ejecutamos:
        print(ve) # imprimimos ve (ValueError)
        return False # regresamos False

        
try: # "intento"
    print(palindrome("")) # valor de la funcion = "vacio"
    print(palindrome(1))# valor de la funcion = numero
except TypeError: # error de excepción
    print("Solo se pueden ingresar letras (palabras): ") # solo strings

#----------------------------------------

# def palindrome(string):
#     return string == string [::-1] # regresa el string si es igual a si mismo alrevez

# try: # "intento"
#     print(palindrome(""))
#     # print(palindrome(1)) # valor de la funcion = numero
# except TypeError: # error de excepción
#     print("Solo se pueden ingresar palabras") # solo strings