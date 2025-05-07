import sqlite3

def get_connection():
    return sqlite3.connect('funcionarios.db')

def populate_database():
    funcionarios = [
        ('Cédula', '1234567890', 'Juan', 'Pérez', 'Casado', 'M', 'Calle 123', '555-0101', '1980-05-15'),
        ('Cédula', '2345678901', 'María', 'González', 'Soltera', 'F', 'Avenida 456', '555-0102', '1985-08-20'),
        ('Pasaporte', 'AB123456', 'Carlos', 'Rodríguez', 'Casado', 'M', 'Carrera 789', '555-0103', '1975-03-10'),
        ('Cédula', '3456789012', 'Ana', 'Martínez', 'Divorciada', 'F', 'Calle 321', '555-0104', '1990-11-25'),
        ('Pasaporte', 'CD789012', 'Pedro', 'López', 'Soltero', 'M', 'Avenida 654', '555-0105', '1988-07-30')
    ]

    familiares = [
        (1, 'Laura Pérez', 'Esposa', 38),
        (1, 'Juanito Pérez', 'Hijo', 10),
        (2, 'José González', 'Padre', 65),
        (3, 'Carmen Rodríguez', 'Esposa', 45),
        (3, 'Carlitos Rodríguez', 'Hijo', 15),
        (4, 'Roberto Martínez', 'Ex-esposo', 45),
        (4, 'Sofía Martínez', 'Hija', 12),
        (5, 'María López', 'Madre', 70)
    ]

    estudios = [
        (1, 'Universidad Nacional', 'Pregrado', 'Ingeniería de Sistemas'),
        (1, 'Universidad de los Andes', 'Maestría', 'Maestría en Informática'),
        (2, 'Universidad Javeriana', 'Pregrado', 'Administración de Empresas'),
        (3, 'Universidad del Rosario', 'Pregrado', 'Derecho'),
        (3, 'Universidad Externado', 'Especialización', 'Derecho Laboral'),
        (4, 'Universidad de Antioquia', 'Pregrado', 'Medicina'),
        (5, 'Universidad Industrial de Santander', 'Pregrado', 'Ingeniería Civil')
    ]

    try:
        conn = get_connection()
        cursor = conn.cursor()

        print("Insertando funcionarios...")
        for funcionario in funcionarios:
            cursor.execute('''
                INSERT INTO funcionario 
                (tipo_identificacion, numero_identificacion, nombres, apellidos, estado_civil, sexo, direccion, telefono, fecha_nacimiento)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', funcionario)

        print("Insertando familiares...")
        for familiar in familiares:
            cursor.execute('''
                INSERT INTO grupo_familiar 
                (id_funcionario, nombre, parentesco, edad)
                VALUES (?, ?, ?, ?)
            ''', familiar)

        print("Insertando información académica...")
        for estudio in estudios:
            cursor.execute('''
                INSERT INTO informacion_academica 
                (id_funcionario, universidad, nivel_estudio, titulo)
                VALUES (?, ?, ?, ?)
            ''', estudio)

        conn.commit()
        print("¡Base de datos poblada exitosamente!")

    except sqlite3.Error as e:
        print(f"Error al poblar la base de datos: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    populate_database() 