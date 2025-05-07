import sqlite3
from models.funcionario import Funcionario
from exceptions.dao_exception import DAOException
from db.conexion import get_connection

class FuncionarioDAO:
    def __init__(self, db_path='funcionarios.db'):
        self.db_path = db_path

    def conectar(self):
        return get_connection()

    def crear(self, funcionario: Funcionario):
        try:
            con = self.conectar()
            cur = con.cursor()
            cur.execute('''
                INSERT INTO funcionario 
                (tipo_identificacion, numero_identificacion, nombres, apellidos, estado_civil, sexo, direccion, telefono, fecha_nacimiento)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (funcionario.tipo_identificacion, funcionario.numero_identificacion, funcionario.nombres,
                  funcionario.apellidos, funcionario.estado_civil, funcionario.sexo, funcionario.direccion,
                  funcionario.telefono, funcionario.fecha_nacimiento))
            con.commit()
        except Exception as e:
            raise DAOException(f"Error al crear funcionario: {e}")
        finally:
            con.close()

    def listar_todos(self):
        try:
            con = self.conectar()
            cur = con.cursor()
            cur.execute('SELECT * FROM funcionario')
            filas = cur.fetchall()
            return [Funcionario(*fila) for fila in filas]
        except Exception as e:
            raise DAOException(f"Error al listar funcionarios: {e}")
        finally:
            con.close()

    def actualizar(self, funcionario: Funcionario):
        try:
            con = self.conectar()
            cur = con.cursor()
            cur.execute('''
                UPDATE funcionario
                SET tipo_identificacion=?, numero_identificacion=?, nombres=?, apellidos=?, estado_civil=?, 
                    sexo=?, direccion=?, telefono=?, fecha_nacimiento=?
                WHERE id_funcionario=?
            ''', (funcionario.tipo_identificacion, funcionario.numero_identificacion, funcionario.nombres,
                  funcionario.apellidos, funcionario.estado_civil, funcionario.sexo, funcionario.direccion,
                  funcionario.telefono, funcionario.fecha_nacimiento, funcionario.id_funcionario))
            con.commit()
        except Exception as e:
            raise DAOException(f"Error al actualizar funcionario: {e}")
        finally:
            con.close()

    def eliminar(self, id_funcionario: int):
        try:
            con = self.conectar()
            cur = con.cursor()
            cur.execute('DELETE FROM funcionario WHERE id_funcionario=?', (id_funcionario,))
            con.commit()
        except Exception as e:
            raise DAOException(f"Error al eliminar funcionario: {e}")
        finally:
            con.close()
