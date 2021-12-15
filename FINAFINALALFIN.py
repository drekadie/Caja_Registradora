cantidades=[]
finalizar="@"
articulos=[]
costo1=[]
formula=""
costo2=[]


def lector_producto_precio():
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("                  □♡□♡□♡□♡□♡□♡□♡TIENDA DEL LOCO MARIO♡□♡□♡□♡□♡□♡□♡□"            )
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("                                     ACA VOTAMOS 1"                                    )
    print("                             todos para uno, uno para todos \n"                        )
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    while True:
        producto=input("            SI ES TAN AMABLE MI QUERIDO CAJERO, ESCRIBA EL PRODUCTO A INGRESAR: \n")
        producto=producto.upper()
        articulos.append(producto)

        cantidad=int(input("        AHORA INGRESE LA CANTIDAD \n  "))
        cantidades.append(cantidad)

        precio=int(input("          AHORA PORFAVOR INGRESE EL VALOR DEL ARTICULO:  \n"))
        costo1.append(precio)
        precio=precio * cantidad
        costo2.append(precio)

        formula=input("             SI DESEAS AGREGAR MAS ARTICULOS APRETA <ENTER> DE LO CONTRARIO ESCRIBE NO: \n")
        formula=formula.upper()

        if formula == "NO":
            break


def procesar_pago():
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*            BOLETA            .¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    for a,b,c,d in zip(articulos, costo1, cantidades, costo2):
        print(a,"UN",b,"X", c, "$",d)

    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    precio_total = sum(costo2)
    print("TOTAL $", precio_total, "pesos")
    total_iva = precio_total * 1.19

    iva = total_iva - precio_total
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("IVA $", round(iva), "pesos")
    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    print("TOTAL A PAGAR DEL CLIENTE $", round(total_iva), "pesos") 

    print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
    while True:
        pago = int(input('CON CUANTO PAGA EL CLIENTE $: '))
        if pago >= total_iva :
            vuelto = pago - total_iva
            print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
            print('VUELTO DEL CLIENTE ES $', vuelto, ' pesos')
            print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")
            terminar = input("PRESIONE <ENTER> PARA QUE TERMINE TODO AL FIN: ")
            print("¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸¸.•*¨*•.¸♪¸.•*¨*•.¸♥¸.•*¨*•.¸")

            if terminar == "":
                break

        elif pago < total_iva and pago > 0 :
            print('                                           ')
            print('SI NO TIENE PLATA QUE VAYA A LA CASA POR MAS, PARA CANCELAR TODO ESCRIBA EL NUMERO 0 Y APRETE <ENTER>')
            print('                                           ')

        else:
            print('                                           ')
            break
   

def run ():
    while True:
        lector_producto_precio()
        procesar_pago()
    


if __name__ == "__main__":
    run()