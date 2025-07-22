list_sale_day = []
high_sale = []
low_sale = []
mid_sale = []

while True:
    print(f"MENÚ DE ANÁLISIS DE VENTAS")
    print(f"1. Ingresar lista de ventas")
    print(f"2. Mostrar todas las ventas realizadas")
    print(f"3. Calcular venta más alta y baja")
    print(f"4. Promedio de ventas")
    print(f"5. Dias de buena venta")
    print(f"6. Clasificacion de ventas")
    print(f"7. Salir")
    option_user = input(f"Ingrese una opción: ")

    match option_user:
        case "1":
            print(f"\nIngresar lista de ventas")
            days_sale = int(input(f"Ingrese cuantos dias de venta registrara: "))
            i = 0
            for i in range(1, days_sale+1):
                while True:
                    price_day = input(f"Ingrese la venta del día {i} en numeros enteros: Q")
                    if price_day.isdigit():
                        price_day_right = int(price_day)
                        if price_day_right >= 0:
                            list_sale_day.append(price_day_right)
                        else:
                            print(f"No ingreso un número entero positivo")
                        break
                    else:
                        print("Ingrese un número entero positivo")

        case "2":
            print(f"\nMostrar todas las ventas realizadas")
            for j in range(len(list_sale_day)):
                print(f"Venta día {j+1} = Q{list_sale_day[j]}")
            print(f"")

        case "3":
            print(f"\nVenta más baja y alta")
            print(f"La venta más alta fue de Q{max(list_sale_day)}")
            print(f"La venta más alta fue de Q{min(list_sale_day)}\n")

        case "4":
            print(f"\nPromedio de ventas")
            print(f"El promedio de las ventas son de Q{sum(list_sale_day)/len(list_sale_day)}\n")

        case "5":
            print(f"\nDias de buena venta")
            count_value = 0
            print(f"\nDias de buena venta")
            for k in list_sale_day:
                if k > 1000:
                    count_value += 1
            print(f"El total de ventas mayores a Q1000 son de ({count_value}) veces\n")

        case "6":
            print(f"\nClasificacion de ventas")

        case "7":
            print(f"\nSalio del programa...")
            break

        case _:
            print(f"\nIngreso mal un valor")