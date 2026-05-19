# Diccionario que almacena todos los videojuegos
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

# ============================================
# FUNCIONES DEL SISTEMA
# ============================================

def agregar_videojuego(videojuegos):
    """Agregar un nuevo videojuego al inventario."""
    # Solicita los datos del nuevo videojuego
    codigo = input("Ingrese el codigo del videojuego (ej: VG004): ").strip().upper()
    
    # Validación: no permitir códigos duplicados
    if codigo in videojuegos:
        print("Error: El codigo ya existe.")
        return
    
    nombre = input("Ingrese el nombre del videojuego: ").strip()
    plataforma = input("Ingrese la plataforma (PC, PlayStation, Xbox, Nintendo): ").strip()
    
    try:
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad en inventario: "))
        
        # Validación: precio y cantidad deben ser mayores a cero
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser mayores que cero.")
            return
    except ValueError:
        print("Error: Ingrese valores numericos validos.")
        return
    
    # Agregar el nuevo videojuego al diccionario
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"Videojuego {codigo} agregado exitosamente.")

def mostrar_inventario(videojuegos):
    """Mostrar todos los videojuegos registrados en el inventario."""
    if not videojuegos:
        print("No hay videojuegos en el inventario.")
        return
    
    print("\n===== INVENTARIO COMPLETO =====")
    for codigo, info in videojuegos.items():
        print(f"Codigo: {codigo}")
        print(f"  Nombre: {info['nombre']}")
        print(f"  Plataforma: {info['plataforma']}")
        print(f"  Precio: ${info['precio']:,}")
        print(f"  Cantidad: {info['cantidad']}")
        print("-" * 40)

def buscar_videojuego(videojuegos):
    """Buscar y mostrar la información de un videojuego por su código."""
    codigo = input("Ingrese el codigo del videojuego: ").strip().upper()
    
    if codigo in videojuegos:
        info = videojuegos[codigo]
        print(f"\nInformacion de {codigo}:")
        print(f"Nombre: {info['nombre']}")
        print(f"Plataforma: {info['plataforma']}")
        print(f"Precio: ${info['precio']:,}")
        print(f"Cantidad: {info['cantidad']}")
    else:
        print("Videojuego no encontrado.")

def actualizar_precio(videojuegos):
    """Actualizar el precio de un videojuego existente."""
    codigo = input("Ingrese el codigo del videojuego: ").strip().upper()
    
    if codigo not in videojuegos:
        print("Videojuego no encontrado.")
        return
    
    try:
        nuevo_precio = int(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("El precio debe ser mayor que cero.")
            return
        
        videojuegos[codigo]["precio"] = nuevo_precio
        print(f"Precio actualizado correctamente a ${nuevo_precio:,}")
    except ValueError:
        print("Error: Ingrese un valor numerico valido.")

def registrar_venta(videojuegos):
    """Registrar una venta, actualizar inventario y mostrar factura."""
    codigo = input("Ingrese el codigo del videojuego: ").strip().upper()
    
    if codigo not in videojuegos:
        print("Videojuego no encontrado.")
        return
    
    try:
        cantidad_vender = int(input("Ingrese la cantidad a vender: "))
        if cantidad_vender <= 0:
            print("La cantidad debe ser mayor que cero.")
            return
    except ValueError:
        print("Error: Ingrese un numero valido.")
        return
    
    info = videojuegos[codigo]
    
    # Validar stock disponible
    if cantidad_vender > info["cantidad"]:
        print(f"Inventario insuficiente. Solo hay {info['cantidad']} unidades.")
        return
    
    # Realizar la venta
    total = info["precio"] * cantidad_vender
    info["cantidad"] -= cantidad_vender
    
    # Mostrar factura
    print("\n" + "="*40)
    print("               FACTURA")
    print("="*40)
    print(f"Juego: {info['nombre']}")
    print(f"Precio unitario: ${info['precio']:,}")
    print(f"Cantidad: {cantidad_vender}")
    print(f"Total: ${total:,}")
    print("="*40)
    
    # Descuento opcional
    if total > 500000:
        print("Descuento del 10% aplicado por compra mayor a $500.000!")
        print(f"Total con descuento: ${int(total * 0.9):,}")

def mostrar_estadisticas(videojuegos):
    """Mostrar estadísticas generales del inventario."""
    if not videojuegos:
        print("No hay datos para mostrar estadisticas.")
        return
    
    total_juegos = len(videojuegos)
    valor_total = sum(info["precio"] * info["cantidad"] for info in videojuegos.values())
    
    # Videojuego más caro
    mas_costoso = max(videojuegos.items(), key=lambda x: x[1]["precio"])
    # Videojuego con más stock
    mayor_cantidad = max(videojuegos.items(), key=lambda x: x[1]["cantidad"])
    # Promedio de precios
    promedio_precio = sum(info["precio"] for info in videojuegos.values()) / total_juegos
    
    print("\n===== ESTADISTICAS =====")
    print(f"Total de videojuegos registrados: {total_juegos}")
    print(f"Valor total del inventario: ${valor_total:,}")
    print(f"Videojuego mas costoso: {mas_costoso[1]['nombre']} (${mas_costoso[1]['precio']:,})")
    print(f"Videojuego con mas stock: {mayor_cantidad[1]['nombre']} ({mayor_cantidad[1]['cantidad']} unidades)")
    print(f"Promedio de precios: ${promedio_precio:,.0f}")

def eliminar_videojuego(videojuegos):
    """Eliminar un videojuego del inventario después de confirmación."""
    codigo = input("Ingrese el codigo del videojuego a eliminar: ").strip().upper()
    
    if codigo in videojuegos:
        confirmacion = input(f"Esta seguro de eliminar {videojuegos[codigo]['nombre']}? (s/n): ").strip().lower()
        if confirmacion == 's':
            del videojuegos[codigo]
            print("Videojuego eliminado correctamente.")
        else:
            print("Operacion cancelada.")
    else:
        print("Videojuego no encontrado.")

def menu():
    """Mostrar el menú principal y controlar el flujo del programa."""
    while True:
        print("\n" + "="*35)
        print("   TIENDA DE VIDEOJUEGOS")
        print("="*35)
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por codigo")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadisticas")
        print("7. Eliminar videojuego")
        print("8. Salir")
        print("="*35)
        
        opcion = input("Seleccione una opcion (1-8): ").strip()
        
        if opcion == "1":
            agregar_videojuego(videojuegos)
        elif opcion == "2":
            mostrar_inventario(videojuegos)
        elif opcion == "3":
            buscar_videojuego(videojuegos)
        elif opcion == "4":
            actualizar_precio(videojuegos)
        elif opcion == "5":
            registrar_venta(videojuegos)
        elif opcion == "6":
            mostrar_estadisticas(videojuegos)
        elif opcion == "7":
            eliminar_videojuego(videojuegos)
        elif opcion == "8":
            print("Gracias por usar el sistema de gestion de la tienda!")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

# ============================================
# EJECUCIÓN DEL PROGRAMA
# ============================================
if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestion de Tienda de Videojuegos")
    menu()