def decorador(funcionB):
    def funcionC(*args, **kwargs):
        print("Iniciando la ejecucion de la funcion")
        resultado = funcionB(*args, **kwargs)
        print("Suma de los parametros la funcionB: {}".format(sum(args)))
        print("Resultado de la multiplicacion: {}".format(resultado))
        print("Finalizando la ejecucion de la funcion")
        return resultado
    return funcionC


@decorador
def multiplica(a, b, c, d):
    producto = a*b*c*d
    return producto


multiplica(1, 2, 3, 4)
multiplica(5, 6, 10, 10)
multiplica(1, 22, 53, 12)
