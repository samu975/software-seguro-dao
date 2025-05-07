import sqlite3

def init_db():
    conexion = sqlite3.connect('funcionarios.db')
    cursor = conexion.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionario (
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_identificacion TEXT,
        numero_identificacion TEXT UNIQUE,
        nombres TEXT,
        apellidos TEXT,
        estado_civil TEXT,
        sexo TEXT,
        direccion TEXT,
        telefono TEXT,
        fecha_nacimiento TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grupo_familiar (
        id_familiar INTEGER PRIMARY KEY AUTOINCREMENT,
        id_funcionario INTEGER,
        nombre TEXT,
        parentesco TEXT,
        edad INTEGER,
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario) ON DELETE CASCADE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS informacion_academica (
        id_academica INTEGER PRIMARY KEY AUTOINCREMENT,
        id_funcionario INTEGER,
        universidad TEXT,
        nivel_estudio TEXT,
        titulo TEXT,
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario) ON DELETE CASCADE
    )
    ''')

    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    init_db()
