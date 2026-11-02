import sqlite3

conexion = sqlite3.connect(r"C:\Users\Estudiante\Downloads\TP ALP\juegos.db")
cursor = conexion.cursor()

print("TABLAS ENCONTRADAS:")
print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())

def consultar():
    cursor.execute("SELECT * FROM Juegos")
    print(cursor.fetchall())

def buscar():
    id = input("Ingrese el ID: ")
    cursor.execute("SELECT * FROM Juegos WHERE id = ?", (id,))
    print(cursor.fetchone())

def agregar():
    nombre = input("Nombre: ")
    genero = input("Genero: ")
    plataforma = input("Plataforma: ")
    precio = float(input("Precio: "))

    cursor.execute(
        "INSERT INTO Juegos (nombre, genero, plataforma, precio) VALUES (?, ?, ?, ?)",
        (nombre, genero, plataforma, precio)
    )
    conexion.commit()
    print("Juego agregado.")

def actualizar():
    id = input("ID del juego: ")
    nombre = input("Nuevo nombre: ")
    genero = input("Nuevo genero: ")
    plataforma = input("Nueva plataforma: ")
    precio = float(input("Nuevo precio: "))

    cursor.execute(
        "UPDATE Juegos SET nombre=?, genero=?, plataforma=?, precio=? WHERE id=?",
        (nombre, genero, plataforma, precio, id)
    )
    conexion.commit()
    print("Juego actualizado.")

def eliminar():
    id = input("ID del juego: ")
    cursor.execute("DELETE FROM Juegos WHERE id=?", (id,))
    conexion.commit()
    print("Juego eliminado.")

while True:
    print("""
    1) Consultar juegos
    2) Buscar juego
    3) Agregar juego
    4) Actualizar juego
    5) Eliminar juego
    6) Salir
    """)

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        consultar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        agregar()
    elif opcion == "4":
        actualizar()
    elif opcion == "5":
        eliminar()
    elif opcion == "6":
        break
    else:
        print("Opcion incorrecta.")

conexion.close()
