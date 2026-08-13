import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import PIL
def procrut(stroki: int,stolbci: int):
    new_lst=[]
    result_procruta=[]
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
    #1 combination(full row)
    result_bool2 = False
    for b in result:
        result_bool1 = True
        for c in range(stroki):
            if b[c]>0.5:
                result_bool1=result_bool1 and True
            else:
                result_bool1=False
        result_bool2=result_bool1 or result_bool2
    ###!MAKE MORE COMBINATIONS(list of 30)!###
    #n combination (full axis)-negative
    # for d in range(len(result)):
    #     if result[0][d] and result[1][d] and result[2][d] > 0.5:
    #         result_bool=True
    return result_bool2

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
root.title("BurmApp")

#Иконка приложения и прочие картинки
icon_image = Image.open("BurmAppIcon.png")
tk_icon = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, tk_icon)

background=Image.open("background_grey.png")
background_image=ImageTk.PhotoImage(background)
label=tk.Label(root,image=background_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
#фрукты
slyva=Image.open("slyva.png")
slyva_image=ImageTk.PhotoImage(slyva)
yabloko=Image.open("yabloko.png")
yabloko_image=ImageTk.PhotoImage(yabloko)
vinograd=Image.open("vinograd.png")
vinograd_image=ImageTk.PhotoImage(vinograd)
banany=Image.open("banany.png")
banany_image=ImageTk.PhotoImage(banany)
award_coin=Image.open("award_coin.png")
awward_coin_image=ImageTk.PhotoImage(award_coin)


#начальный прокрут
start_list=[]
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)
for a in range(3):
    new_lst=[random.random() for _ in range(stolbci)]
    start_list.append(new_lst)
for r in range(3):
    for c in range(3):
        label = tk.Label(text=f"{round(start_list[r][c],3)}")
        label.grid(row=r, column=c)


#ФУНКЦИОНАЛ И ВНУТРЕННИЙ ИНТЕРФЕЙС
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

#root.attributes("-toolwindow", True) # через attributes можно прописывать всякие доп.фишки
#!есть еще ttk-кастомный чуть более профессиональный tk со своими правилами
clicks = 0


def click_button():#обработчик клика?
    result=[]
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    result=procrut(3,3)
    check_combinations(result)
    for c in range(3): root.columnconfigure(index=c, weight=1)
    for r in range(3): root.rowconfigure(index=r, weight=1)
    for r in range(3):
        for c in range(3):
            if result[r][c]<=0.22:
                label = tk.Label(image=slyva_image)
                label.grid(row=r, column=c)
            if result[r][c]>0.22 and result[r][c]<=0.44:
                label = tk.Label(image=yabloko_image)
                label.grid(row=r, column=c)
            if result[r][c]>0.44 and result[r][c]<=0.66:
                label = tk.Label(image=vinograd_image)
                label.grid(row=r, column=c)
            if result[r][c]>0.66 and result[r][c]<=0.88:
                label = tk.Label(image=banany_image)
                label.grid(row=r, column=c)
            if result[r][c]>0.88:
                label = tk.Label(image=award_coin_image)
                label.grid(row=r, column=c)

    result_final=""
    if check_combinations(result):
        result_final="WIN"
    else:
        result_final="LOSE"
    btn["text"] = f"{result_final}"
btn=tk.Button(text="Play",command=click_button)#создание кнопки с подкрученным обработчиком клика
#btn = ttk.Button(text="Click Me", state=["disabled"]) #можно еще гасить кнопку через состояния state
btn.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=5)#Размещение кнопки




root.mainloop()#метод для отображения окна для пользователя