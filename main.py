import tkinter as tk
import random

result_procruta = []
def procrut(stroki: int,stolbci: int):
    list_with_numbers=[random.random() for _ in range (stroki*stolbci)]
    for i in range(stroki):
            new_lst=[random.random() for _ in range(stolbci)]
            result_procruta.append(new_lst)
    return result_procruta
#stroki=int(input())
#stolbci=int(input())
stroki=3;stolbci=3
result=procrut(stroki,stolbci)
for i in range(3):
    print(result[i])

# root=tk.Tk()
# root.title("Window")
# root.geometry("800x600")
# label=tk.Label(root, text="Hello,World!")
# label.pack()
# root.mainloop()