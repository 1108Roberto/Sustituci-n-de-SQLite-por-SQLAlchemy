from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la conexión a MariaDB
DATABASE_URL = "mysql+pymysql://usuario:contraseña@localhost/recetas_db"

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear la base para los modelos
Base = declarative_base()

# Definir el modelo de Receta
class Receta(Base):
    __tablename__ = 'recetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    ingredientes = Column(String(255))
    pasos = Column(String(255))

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ")
    pasos = input("Ingrese los pasos: ")
    receta = Receta(nombre=nombre, ingredientes=ingredientes, pasos=pasos)
    session.add(receta)
    session.commit()
    print("Receta agregada exitosamente.")

def actualizar_receta():
    id = int(input("Ingrese el ID de la receta que desea actualizar: "))
    receta = session.query(Receta).filter_by(id=id).first()
    if receta:
        receta.nombre = input("Ingrese el nuevo nombre de la receta: ")
        receta.ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ")
        receta.pasos = input("Ingrese los nuevos pasos: ")
        session.commit()
        print("Receta actualizada exitosamente.")
    else:
        print("Receta no encontrada.")

def eliminar_receta():
    id = int(input("Ingrese el ID de la receta que desea eliminar: "))
    receta = session.query(Receta).filter_by(id=id).first()
    if receta:
        session.delete(receta)
        session.commit()
        print("Receta eliminada exitosamente.")
    else:
        print("Receta no encontrada.")

def ver_recetas():
    recetas = session.query(Receta).all()
    if recetas:
        for receta in recetas:
            print(f"ID: {receta.id}, Nombre: {receta.nombre}")
    else:
        print("No hay recetas disponibles.")

def buscar_receta():
    id = int(input("Ingrese el ID de la receta que desea buscar: "))
    receta = session.query(Receta).filter_by(id=id).first()
    if receta:
        print(f"Nombre: {receta.nombre}")
        print(f"Ingredientes: {receta.ingredientes}")
        print(f"Pasos: {receta.pasos}")
    else:
        print("Receta no encontrada.")

def main():
    while True:
        print("\nOpciones:")
        print("1) Agregar nueva receta")
        print("2) Actualizar receta existente")
        print("3) Eliminar receta existente")
        print("4) Ver listado de recetas")
        print("5) Buscar ingredientes y pasos de receta")
        print("6) Salir")
        
        opcion = input("Seleccione una opción: ").lower()

        if opcion == '1':
            agregar_receta()
        elif opcion == '2':
            actualizar_receta()
        elif opcion == '3':
            eliminar_receta()
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            buscar_receta()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
    session.close()
