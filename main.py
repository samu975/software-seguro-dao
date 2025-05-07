import tkinter as tk
from ui.main_window import FuncionarioApp
from db.init_db import init_db

def main():
    try:
        init_db()
        root = tk.Tk()
        app = FuncionarioApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()