# coding: utf8

import os
import tkinter as tk
import sqlite3
import zipfile
import wmi
from tkinter import ttk
from tkinter.filedialog import askopenfilename


PROG_NAME = 'Бэкапер 1С'
PROG_VER = '0.0.1'
AUTOR = 'Давид Чак'
AUTOR_EMAIL = 'davidchak@yandex.ru'
BASEDIR = os.path.abspath(os.path.dirname(__name__))
DATABASE = 'base.db'

color_theme_1 = {'top': '#FFF7B4', 'menu_text': '#35B495', 'bottom': '#FFF7B4',
                 'center1': '#FEFDFF', 'center2': '#FFFFE3',
                 'button1': '#FFFFE3', 'button2': '#FFFFE3',
                 'selected1': '#FEF659', 'selected2': '#FFF9B9',
                 'border_selected': '#FAF2A7'}

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg=color_theme_1['top'], bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        buttons = [#{'image': 'main.gif', 'command': self.test_msg},
                   {'image': 'add.gif', 'command': self.open_file_dialog_screen},
                  # {'image': 'search.gif', 'command': self.test_msg},
                   {'image': 'scheduler.gif', 'command': self.open_scheduler_screen},
                  # {'image': 'update.gif', 'command': self.test_msg},
                   {'image': 'info.gif', 'command': self.open_info_screen}]

        for index, item in enumerate(buttons):
            icon = tk.PhotoImage(
                file='icons/{}'.format(buttons[index]['image']))
            button = tk.Button(toolbar, image=icon, width=50, height=50,
                               bg=color_theme_1['button2'], command=buttons[index]['command'])
            button.image = icon
            button.pack(side='left', padx=4, pady=2)

        tree = ttk.Treeview(self, columns=(
            'id', 'base', 'path'), show='headings')
        tree.column('id', width=20)
        tree.column('base', width=250)
        tree.column('path', width=315)

        tree.heading('id', text='id')
        tree.heading('base', text='base')
        tree.heading('path', text='path')
        tree.pack(fill='both',  pady=2, padx=2)

    def open_info_screen(self):
        InfoScreen()

    def open_file_dialog_screen(self):
        file_name = askopenfilename(filetypes=(("1C files", "*.1CD"),
                                           ("All files", "*.*")))
        if file_name:
            try:
                # print("""here it comes: self.settings["template"].set(fname)""")
                print(file_name)
            except:
                showerror("Open Source File",
                          "Failed to read file\n'%s'" % fname)
            return

    def open_scheduler_screen(self):
        Scheduler()


class Scheduler(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_scheduler()

    def init_scheduler(self):
        self.title('Планировшик')
        self.geometry('400x220')
        self.resizable(False, False)
        lb = tk.Label(self, text='Планировщик заданий').pack(anchor='center')
        self.grab_set()
        self.focus_set()


class FileDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_file_dialog()

    def init_info(self):
        self.title('Добавление файла')
        self.geometry('400x220')
        self.resizable(False, False)
        
        self.grab_set()
        self.focus_set()


class InfoScreen(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_info()

    def init_info(self):
        self.title('Информация')
        self.geometry('400x220')
        self.resizable(False, False)
        label = tk.Label(text='''Лицензия GPL
        Автор: {1}''')
        self.grab_set()
        self.focus_set()


        



if __name__== '__main__':

    root = tk.Tk()
    ui = Main(root)
    ui.pack()
    root.geometry('600x450')
    root.resizable(width=False, height=False)
    root.title('{}   версия: {} '.format(PROG_NAME, PROG_VER))
    root.iconbitmap(default='icons/1s_icon.ico')
    root.mainloop()

