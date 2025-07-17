stock = {
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}
productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
def stock_marca():
    print("\n--Stock de marca--")
    for clave, datos in productos.items():
        nombre = clave
        print(f"Clave: {clave}, Nombre: {datos[0]}")

def busqueda_precio():
    print("\n--Stock--")
    clave = input("Ingrese la clave del modelo que desea: ").strip()
    encontrado = False
    for clave in stock.items():
        if clave in stock:
            print("Modelo encontrado")
            encontrado = True
        if encontrado:
            try:
                cantidad = int(input("Ingrese la cantidad de dinero que dispone: "))
                if cantidad <= 0:
                    print("Debe ser mayor que 0")
            except ValueError:
                print("Deben ser valores enteros!!!")
                return
            
def actualizar_precio():
    clave = input("Ingrese la clave del modelo que desea actualizar precio: ").strip()
    if clave not in stock:
        print("Modelo no encontrado.")
        return
    if clave in stock:
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio:"))

        except ValueError:
            print("Debe ser un valor valido.")


def menu():
    opcion = 0
    while opcion != 4:
        print("\n--MENU--")
        print("1. Stock Marca")
        print("2. Busqueda por Precio")
        print("3. Actualizar precio")
        print("4. Salir")
        opcion = input("Ingrese la opcion que desea(1 a 4): ")
        if opcion == "1":
            stock_marca()
        elif opcion == "2":
            busqueda_precio()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            print("Programa Finalizado.")
            break
        else:
            print("Opcion invalida. intente nuevamente.")
            continue
menu()
