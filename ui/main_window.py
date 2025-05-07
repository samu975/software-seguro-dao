import tkinter as tk
from tkinter import messagebox
from dao.funcionario_dao import FuncionarioDAO
from models.funcionario import Funcionario

class FuncionarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Funcionarios")
        self.dao = FuncionarioDAO()

        self.selected_id = None

        # Campos del formulario
        self.inputs = {}
        campos = [
            ("Tipo Identificación", "tipo_identificacion"),
            ("Número Identificación", "numero_identificacion"),
            ("Nombres", "nombres"),
            ("Apellidos", "apellidos"),
            ("Estado Civil", "estado_civil"),
            ("Sexo", "sexo"),
            ("Dirección", "direccion"),
            ("Teléfono", "telefono"),
            ("Fecha Nacimiento", "fecha_nacimiento")
        ]

        for idx, (label_text, key) in enumerate(campos):
            tk.Label(root, text=label_text).grid(row=idx, column=0, padx=5, pady=5, sticky='e')
            entry = tk.Entry(root)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            self.inputs[key] = entry

        # Botones
        tk.Button(root, text="Crear", command=self.crear_funcionario).grid(row=0, column=2, padx=5)
        tk.Button(root, text="Actualizar", command=self.actualizar_funcionario).grid(row=1, column=2, padx=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_funcionario).grid(row=2, column=2, padx=5)
        tk.Button(root, text="Limpiar", command=self.limpiar_campos).grid(row=3, column=2, padx=5)

        # Lista de funcionarios
        self.lista = tk.Listbox(root, width=100)
        self.lista.grid(row=10, column=0, columnspan=3, pady=10)
        self.lista.bind('<<ListboxSelect>>', self.on_select)

        self.cargar_funcionarios()

    def crear_funcionario(self):
        try:
            f = self.obtener_datos_formulario()
            self.dao.crear(f)
            messagebox.showinfo("Éxito", "Funcionario creado correctamente.")
            self.cargar_funcionarios()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_funcionario(self):
        if self.selected_id is None:
            messagebox.showwarning("Atención", "Seleccione un funcionario.")
            return
        try:
            f = self.obtener_datos_formulario()
            f.id_funcionario = self.selected_id
            self.dao.actualizar(f)
            messagebox.showinfo("Éxito", "Funcionario actualizado.")
            self.cargar_funcionarios()
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_funcionario(self):
        if self.selected_id is None:
            messagebox.showwarning("Atención", "Seleccione un funcionario.")
            return
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este funcionario?"):
            try:
                self.dao.eliminar(self.selected_id)
                messagebox.showinfo("Éxito", "Funcionario eliminado.")
                self.cargar_funcionarios()
                self.limpiar_campos()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def cargar_funcionarios(self):
        self.lista.delete(0, tk.END)
        funcionarios = self.dao.listar_todos()
        for f in funcionarios:
            self.lista.insert(tk.END, f"{f.id_funcionario} - {f}")

    def on_select(self, event):
        if not self.lista.curselection():
            return
        index = self.lista.curselection()[0]
        data = self.lista.get(index)
        self.selected_id = int(data.split(" - ")[0])
        f = next((x for x in self.dao.listar_todos() if x.id_funcionario == self.selected_id), None)
        if f:
            self.inputs["tipo_identificacion"].delete(0, tk.END)
            self.inputs["tipo_identificacion"].insert(0, f.tipo_identificacion)
            self.inputs["numero_identificacion"].delete(0, tk.END)
            self.inputs["numero_identificacion"].insert(0, f.numero_identificacion)
            self.inputs["nombres"].delete(0, tk.END)
            self.inputs["nombres"].insert(0, f.nombres)
            self.inputs["apellidos"].delete(0, tk.END)
            self.inputs["apellidos"].insert(0, f.apellidos)
            self.inputs["estado_civil"].delete(0, tk.END)
            self.inputs["estado_civil"].insert(0, f.estado_civil)
            self.inputs["sexo"].delete(0, tk.END)
            self.inputs["sexo"].insert(0, f.sexo)
            self.inputs["direccion"].delete(0, tk.END)
            self.inputs["direccion"].insert(0, f.direccion)
            self.inputs["telefono"].delete(0, tk.END)
            self.inputs["telefono"].insert(0, f.telefono)
            self.inputs["fecha_nacimiento"].delete(0, tk.END)
            self.inputs["fecha_nacimiento"].insert(0, f.fecha_nacimiento)

    def limpiar_campos(self):
        for entry in self.inputs.values():
            entry.delete(0, tk.END)
        self.selected_id = None

    def obtener_datos_formulario(self):
        return Funcionario(
            tipo_identificacion=self.inputs["tipo_identificacion"].get(),
            numero_identificacion=self.inputs["numero_identificacion"].get(),
            nombres=self.inputs["nombres"].get(),
            apellidos=self.inputs["apellidos"].get(),
            estado_civil=self.inputs["estado_civil"].get(),
            sexo=self.inputs["sexo"].get(),
            direccion=self.inputs["direccion"].get(),
            telefono=self.inputs["telefono"].get(),
            fecha_nacimiento=self.inputs["fecha_nacimiento"].get()
        )
