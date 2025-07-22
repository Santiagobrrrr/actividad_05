list_sale_day = []

while True:
    print(f"MENÚ DE ANÁLISIS DE VENTAS")
    print(f"1. Ingresar lista de ventas")
    print(f"2. Mostrar todas las ventas realizadas")
    print(f"3. Calcular venta más alta y baja")
    print(f"4. Promedio de ventas")
    print(f"5. Dias de buena venta")
    print(f"6. Buscar ventas")
    print(f"7. Clasificacion de ventas")
    print(f"8. Salir")
    option_user = input(f"Ingrese una opción: ")

    match option_user:
        case "1":
            print(f"Ingresar lista de ventas")
            days_sale = int(input(f"Ingrese cuantos dias de venta registrara: "))
            i = 0
            for i in range(1, days_sale+1):
                price_day = int(input(f"Ingrese la venta del día {i}: Q"))
                list_sale_day.append(price_day)

        case "2":
            print(f"Mostrar todas las ventas realizadas")

        case "3":
            print(f"Venta más baja y alta")

        case "4":
            print(f"Promedio de ventas")

        case "5":
            print(f"Dias de buena venta")

        case "6":
            print(f"Buscar ventas")

        case "7":
            print(f"Clasificacion de ventas")

        case "8":
            print(f"Salio del programa...")
            break

        case _:
            print(f"Ingreso mal un valor")