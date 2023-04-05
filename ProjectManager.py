import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Фрейм для размещения выпадающего списка и кнопок
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Label для выпадающего списка
ttk.Label(frame, text="Фильтр по опыту работы:").grid(row=0, column=0, sticky="w")

# Создание выпадающего списка с опциями
option_var = tk.StringVar(value="Любой")
option_menu = ttk.OptionMenu(frame, option_var, "Любой", "Нет опыта", "1-3 года", "3-5 лет", "Более 5 лет")
option_menu.grid(row=0, column=1, sticky="w")

def add_candidate():
    pass

def edit_candidate():
    pass

def save_resume():
    pass

def download_resume():
    pass

def reject_candidate():
    pass

def reopen_candidate():
    pass
    
# Кнопки для управления процессом отбора
ttk.Button(frame, text="Добавить соискателя", command=add_candidate).grid(row=1, column=0, sticky="w")
ttk.Button(frame, text="Редактировать информацию", command=edit_candidate).grid(row=2, column=0, sticky="w")
ttk.Button(frame, text="Сохранить резюме", command=save_resume).grid(row=3, column=0, sticky="w")
ttk.Button(frame, text="Скачать резюме", command=download_resume).grid(row=4, column=0, sticky="w")
ttk.Button(frame, text="Отклонить соискателя", command=reject_candidate).grid(row=5, column=0, sticky="w")
ttk.Button(frame, text="Вернуть в работу", command=reopen_candidate).grid(row=6, column=0, sticky="w")

root.mainloop()
