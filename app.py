# coding: utf8


import os
import tkinter as tk
import sqlite3
import zipfile


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


class Backuper:
    ''' GUI '''

    def __init__(self, root):
        self.root = root
        root.geometry('600x450')
        root.resizable(width=False, height=False)
        root.title('{}   версия: {} '.format(PROG_NAME, PROG_VER))
        root.iconbitmap(default='icons/1s_icon.ico')
        self.menu = self.crete_menu()
        self.command_panel = self.create_command_panel()
        self.main_screen = tk.Frame(root, bg=color_theme_1['center1'])
        self.main_screen.pack(side="top", fill='both', expand=True)
        self.bottom_panel = tk.Frame(
            root, height=20, bg=color_theme_1['bottom'])
        self.bottom_panel.pack(side='bottom', fill='x')

    
    def check_on_start(self):
        if not os.path.isfile(os.path.join(BASEDIR, DATABASE)):
            try:
                con = sqlite3.connect(os.path.join(BASEDIR, DATABASE))
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE 'bases' ('id'	INTEGER PRIMARY KEY AUTOINCREMENT, 'base_1c' TEXT, 'path_to_base' TEXT)")
                con.commit()
                con.close()
            except sqlite3.DatabaseError as err:
                print(err)                                      # TODO: организовать запись в лога
                                                                          
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
        info_menu.add_command(label="О программе",
                              command=self.create_help_screen)
        menubar.add_cascade(label="Справка", menu=info_menu)
        info_menu.add_command(label="Проверка обновлений",
                              command=self.create_update_prog_screen)
        info_menu.add_separator()
        info_menu.add_command(label="Поддержать проект")        # TODO: добавить обработчик
        root.config(menu=menubar)

    def create_command_panel(self):
        top_panel = tk.Frame(self.root, height=30, bg=color_theme_1['top'])
        top_panel.pack(side='top', fill='x')
        buttons = [{'image': 'main.gif', 'command': self.create_first_screen},
                   {'image': 'add.gif', 'command': self.create_add_config_screen},
                   {'image': 'search.gif', 'command': self.create_searcher_1cconf_screen},   
                   {'image': 'scheduler.gif', 'command': self.create_scheduler_screen},
                   {'image': 'update.gif', 'command': self.create_update_prog_screen},
                   {'image': 'info.gif', 'command': self.create_help_screen}]
                   
        for index, item in enumerate(buttons):
            icon = tk.PhotoImage(file='icons/{}'.format(buttons[index]['image']))
            self.button = tk.Button(
                master=top_panel, image=icon, width=50, height=50, bg=color_theme_1['button2'], command=buttons[index]['command'])
            self.button.image = icon
            self.button.pack(side='left', padx=4, pady=2)
            
    def clear_main_screen(self):
        ''' Отчистка фрейма главного экрана от потомков'''
        if self.main_screen.winfo_children():
            for i in self.main_screen.winfo_children():
                i.destroy()

    def create_first_screen(self):
        ''' Создание первичного(главного) фрейма'''
        self.clear_main_screen()
        first_screen = tk.Frame(self.main_screen, bg=color_theme_1['center1'])
        first_screen.pack(side="top", fill='both', expand=True)
        label = tk.Label(first_screen, text='Главный экран')
        label.pack(anchor='center', ipady=30, pady=50)

    def create_update_prog_screen(self):
        ''' Создание фрейма проверки обновлений программы'''
        self.clear_main_screen()
        update_prog_screen = tk.Frame(
            self.main_screen, bg=color_theme_1['center1'])
        update_prog_screen.pack(side="top", fill='both', expand=True)
        label = tk.Label(update_prog_screen, text='update_prog_screen')
        label.pack(anchor='center', ipady=30, pady=50)

    def create_add_config_screen(self):
        ''' Создание фрейма добавления файлов конфигурации 1С'''
        self.clear_main_screen()
        add_config_screen = tk.Frame(
            self.main_screen, bg=color_theme_1['center1'])
        add_config_screen.pack(side="top", fill='both', expand=True)
        label = tk.Label(add_config_screen, text='add_config_screen')
        label.pack(anchor='center', ipady=30, pady=50)

    def create_scheduler_screen(self):
        ''' Создание фрейма добавления расписания заданий'''
        self.clear_main_screen()
        scheduler_screen = tk.Frame(
            self.main_screen, bg=color_theme_1['center1'])
        scheduler_screen.pack(side="top", fill='both', expand=True)
        label = tk.Label(scheduler_screen,
                         text='scheduler_screen')
        label.pack(anchor='center', ipady=30, pady=50)

    def create_searcher_1cconf_screen(self):
        ''' Создание фрейма добавления файлов конфигурации 1С'''
        self.clear_main_screen()
        searcher_1cconf_screen = tk.Frame(
            self.main_screen, bg=color_theme_1['center1'])
        searcher_1cconf_screen.pack(side="top", fill='both', expand=True)
        label = tk.Label(searcher_1cconf_screen,
                         text='searcher_1cconf_screen')
        label.pack(anchor='center', ipady=30, pady=50)

    def create_help_screen(self):
        ''' Создание фрейма информации '''
        self.clear_main_screen()
        help_screen = tk.Frame(self.main_screen, bg=color_theme_1['center1'])
        help_screen.pack(side="top", fill='both', expand=True)
        test_label = tk.Label(
            help_screen, text='''
        Бэкапер 1С предназначен для резервного копирования информационных баз 1С.
        Если вам понравилась программа, напишите отзыв))
        Даже небольшая сумма будет хорошим стимулом к развитию проекта!
            ''')
        test_label.pack(anchor='center', ipady=30, pady=50)
    
    def init_configs(self):
        self.check_on_start()
        self.create_first_screen()
    
    

if __name__=='__main__':
    root = tk.Tk()
    gui = Backuper(root)
    gui.init_configs()
    root.mainloop()
