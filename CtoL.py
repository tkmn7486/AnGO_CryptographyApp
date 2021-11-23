import tkinter as tk
import csv
from tkinter import font

win = tk.Tk()
win.title("AnGO -C to L -")
win.geometry("400x300")
win.configure(bg="black")

def convert_CtoL():
    crypto = input_C.get()
    for word, read in CtoL_first.items():
      crypto = crypto.replace(word, read)
      print(crypto)
    
    Fcrypto = crypto
    lbl3_C["text"] = Fcrypto
    print(Fcrypto)

# CSV読み込み処理
with open('CtoL_first.csv', mode='r') as inp:
    reader = csv.reader(inp)
    CtoL_first = {rows[0]:rows[1] for rows in reader}

# フォント設定
font1 = font.Font(family='Helvetica', size=20, weight='bold')
font2 = font.Font(family='Helvetica', size=12, weight="bold")
font3 = font.Font(size=10)

# 変数定義
crypto = ""
Fcrypto = ""

# GUIデザイン-LtoC-
lbl_C = tk.Label(win, text="AnGO", fg="Green", bg="black", font=font1, height=2)
lbl_C.pack(side="top")

lbl2_C = tk.Label(win, text="言語 ➡ 暗号", bg="black",fg="Green")
lbl2_C.pack()

input_C = tk.Entry(win, bg="#000", fg="Green", font=font3)
input_C.pack()

enterButton_C = tk.Button(win, text=' OK ', command=convert_CtoL ,bg="black" ,fg="Green")
enterButton_C.pack()

resultTitle_C = tk.Label(win, text="---------------------------- Result ----------------------------", fg="Green",bg="black", font=font2, height=5)
resultTitle_C.pack(side="top")

lbl3_C = tk.Label(win, text="---", fg="Green", bg="black")
lbl3_C.pack()

win.mainloop()