import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import PIL
result_procruta = []
def procrut(stroki: int,stolbci: int):
    list_with_numbers=[random.random() for _ in range (stroki*stolbci)]
    for i in range(stroki):
            new_lst=[random.random() for _ in range(stolbci)]
            result_procruta.append(new_lst)
    return result_procruta
stroki=3;stolbci=3
result=procrut(stroki,stolbci)
for i in range(stroki):
    print(result[i])
#combinations=2
def check_combinations(result):
    global result_bool
    result_bool=False
    #1 combination(full row)
    for b in result:
        for c in range(stroki):
            if b[c]>0.5:
                result_bool=True
            else:
                result_bool=False
    ###!MAKE MORE COMBINATIONS(list of 30)!###
    #n combination (full axis)-negative
    # for d in range(len(result)):
    #     if result[0][d] and result[1][d] and result[2][d] > 0.5:
    #         result_bool=True
    return result_bool

if check_combinations(result)==True:
    print("WIN")
else:
    print("LOSE")



#Настройки окна
root=tk.Tk()
root.title("Window")
root.geometry("800x600+350+100")#положение и размер окна
root.resizable(False, False)#запрещаем расстягивать по ширине и высоте
#root.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150
#root.maxsize(400,300)   # максимальные размеры: ширина - 400, высота - 300 на будущее мин и макс размеры окна
label=tk.Label(root, text="Hello,World!")
root.title("BurmApp")

#Иконка приложения
icon_image = Image.open("BurmAppIcon.png")
tk_icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, tk_icon)


#ФУНКЦИОНАЛ И ВНУТРЕННИЙ ИНТЕРФЕЙС
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

#root.attributes("-toolwindow", True) # через attributes можно прописывать всякие доп.фишки
#!есть еще ttk-кастомный чуть более профессиональный tk со своими правилами
clicks = 0


def click_button():#обработчик клика?
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    btn["text"] = f"Played {clicks} games"
btn=tk.Button(text="Play",command=click_button)#создание кнопки с подкрученным обработчиком клика
#btn = ttk.Button(text="Click Me", state=["disabled"]) #можно еще гасить кнопку через состояния state
btn.pack()#Размещение кнопки




label.pack()#текстовая метка
root.mainloop()#метод для отображения окна для пользователя