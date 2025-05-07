import tkinter as tk
from ui.main_window import FuncionarioApp
from db.init_db import init_db

def main():
    init_db()
    root = tk.Tk()
    app = FuncionarioApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()