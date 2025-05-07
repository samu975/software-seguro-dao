# Gestión de Funcionarios

## Descripción
Aplicación de escritorio para la gestión de funcionarios, desarrollada en Python utilizando Tkinter para la interfaz gráfica y SQLite para la base de datos.

## Requisitos
- Python 3.x
- SQLite3
- Tkinter (incluido en la instalación estándar de Python)

## Instalación
1. Clonar el repositorio
2. Navegar al directorio del proyecto
3. Asegurarse de tener Python 3.x instalado

## Uso
Para iniciar la aplicación, ejecutar uno de los siguientes comandos desde el directorio raíz del proyecto:

```bash
python3 main.py
# o
python main.py
```

## Estructura del Proyecto
```
gestion_funcionarios/
├── db/
│   ├── init_db.py      # Script de inicialización de la base de datos
│   ├── populate_db.py  # Script para poblar la base de datos con datos de ejemplo
│   └── conexion.py     # Configuración de la conexión a la base de datos
├── models/
│   ├── funcionario.py
│   ├── grupo_familiar.py
│   └── informacion_academica.py
├── dao/
│   └── funcionario_dao.py
├── exceptions/
│   └── dao_exception.py
├── ui/
│   └── main_window.py
└── main.py
```

## Modelo Relacional

### Tabla: funcionario
```
funcionario (
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
```

### Tabla: grupo_familiar
```
grupo_familiar (
    id_familiar INTEGER PRIMARY KEY AUTOINCREMENT,
    id_funcionario INTEGER,
    nombre TEXT,
    parentesco TEXT,
    edad INTEGER,
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario) ON DELETE CASCADE
)
```

### Tabla: informacion_academica
```
informacion_academica (
    id_academica INTEGER PRIMARY KEY AUTOINCREMENT,
    id_funcionario INTEGER,
    universidad TEXT,
    nivel_estudio TEXT,
    titulo TEXT,
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario) ON DELETE CASCADE
)
```

### Descripción de las Relaciones
- Un funcionario puede tener múltiples familiares (relación 1:N)
- Un funcionario puede tener múltiples registros académicos (relación 1:N)
- La eliminación de un funcionario elimina automáticamente sus registros relacionados (ON DELETE CASCADE)

## Base de Datos
La aplicación utiliza SQLite como base de datos. Los scripts de inicialización y población de datos se ejecutan automáticamente al iniciar la aplicación:

- `init_db.py`: Crea las tablas necesarias en la base de datos
- `populate_db.py`: Inserta datos de ejemplo en las tablas

No es necesario ejecutar estos scripts manualmente, ya que se ejecutan automáticamente al iniciar la aplicación.

## Características
- Gestión de funcionarios (crear, leer, actualizar, eliminar)
- Registro de información familiar
- Registro de información académica
- Interfaz gráfica intuitiva
- Persistencia de datos en base de datos SQLite

## Contribución
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request 