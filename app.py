# coding: utf8


import os
import tkinter as tk
import zipfile


PROG_NAME = 'Бэкапер 1С'
PROG_VER = '0.0.1'
AUTOR = 'Давид Чак'
AUTOR_EMAIL = 'davidchak@yandex.ru'
BASEDIR = os.path.abspath(os.path.dirname(__name__))


color_theme_1 = {'top': '#FFF7B4', 'menu_text': '#35B495', 'bottom': '#FFF7B4',
               'center1': '#FEFDFF', 'center2': '#FFFFE3', 
               'button1': '#FFFFE3', 'button2': '#FFFFE3', 
               'selected1': '#FEF659', 'selected2': '#FFF9B9',
                 'border_selected': '#FAF2A7'}


def search_1c_configs():                # TODO: Написать обработчик
    print('SEARCH !C CONFIG!')


def get_help():                         # TODO: Написать обработчик
    print('HELP PAGE!')


def get_prog_upd():                     # TODO: Написать обработчик
    print('GET PROG UPD!')


class Backuper:
    ''' GUI '''

    def __init__(self, root):
        self.root = root
        root.geometry('600x450')
        root.resizable(width=False, height=False)
        root.title('{}   версия: {} '.format(PROG_NAME, PROG_VER))
        root.iconbitmap(default='icons/1s_icon.ico')
   
    def crete_menu(self):
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0, fg=color_theme_1['menu_text'])
        file_menu.add_command(label="Открыть конфигурацию")     # TODO: добавить обработчик
        file_menu.add_command(label="Сохранить конфигурацию")   # TODO: добавить обработчик
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=root.quit)
        menubar.add_cascade(label="Файл", menu=file_menu)
        config_menu = tk.Menu(menubar, tearoff=0,
                              fg=color_theme_1['menu_text'])
        config_menu.add_command(label="Настройки архиватора")   # TODO: добавить обработчик
        config_menu.add_command(label="Настройки интерфейса")   # TODO: добавить обработчик
        menubar.add_cascade(label="Настройки", menu=config_menu)
        info_menu = tk.Menu(menubar, tearoff=0, fg=color_theme_1['menu_text'])
        info_menu.add_command(label="О программе", command=get_help) 
        menubar.add_cascade(label="Справка", menu=info_menu)
        info_menu.add_command(label="Проверка обновлений", command=get_prog_upd)
        info_menu.add_separator()
        info_menu.add_command(label="Поддержать проект")        # TODO: добавить обработчик
        root.config(menu=menubar)

    def create_command_panel(self):
        top_panel = tk.Frame(self.root, height=30, bg=color_theme_1['top'])
        top_panel.pack(side='top', fill='x')
        buttons = [{'image': 'search.gif', 'command': search_1c_configs},   
                   {'image': 'update.gif', 'command': get_prog_upd},  
                   {'image': 'info.gif', 'command': get_help}]
                   
        for index, item in enumerate(buttons):
            icon = tk.PhotoImage(file='icons/{}'.format(buttons[index]['image']))
            self.button = tk.Button(
                master=top_panel, image=icon, width=50, height=50, bg=color_theme_1['button2'], command=buttons[index]['command'])
            self.button.image = icon
            self.button.pack(side='left', padx=2, pady=2)
            
    def create_main_window(self):
        main_window = tk.Frame(root, bg=color_theme_1['center1'])
        main_window.pack(side="top", fill='both', expand=True)

    def create_bottom_panel(self):
        bottom_panel = tk.Frame(root, height=20, bg=color_theme_1['bottom'])
        bottom_panel.pack(side='bottom', fill='x')

    def init_gui(self):
        self.crete_menu()
        self.create_command_panel()
        self.create_main_window()
        self.create_bottom_panel()

    
if __name__=='__main__':
    root = tk.Tk()
    gui = Backuper(root)
    gui.init_gui()
    root.mainloop()
