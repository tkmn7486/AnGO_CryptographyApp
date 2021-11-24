import tkinter as tk
import csv
from tkinter import font

win = tk.Tk()
win.title("AnGO -C to L -")
win.geometry("450x350")
win.configure(bg="black")

def convert_CtoL():
    crypto = input_C.get()
    for word, read in CtoL_first.items():
      crypto = crypto.replace(word, read)
      print(crypto)

    for word2, read2 in CtoL_second.items():
      crypto = crypto.replace(word2, read2)
      print(crypto)

    for word3, read3 in CtoL_third.items():
      crypto = crypto.replace(word3, read3)
      print(crypto)
    
    Fcrypto = "　"+crypto
    lbl3_C.insert('1.0',Fcrypto)
    print(Fcrypto)

def copyText():
  win.clipboard_clear()
  copy = lbl3_C.get('1.0','end')
  win.clipboard_append(copy)

# CSV読み込み処理
with open('CtoL_first.csv', mode='r') as inp:
    reader = csv.reader(inp)
    CtoL_first = {rows[0]:rows[1] for rows in reader}

with open('CtoL_second.csv', mode='r') as inp:
    reader = csv.reader(inp)
    CtoL_second = {rows[0]:rows[1] for rows in reader}

with open('CtoL_third.csv', mode='r') as inp:
    reader = csv.reader(inp)
    CtoL_third = {rows[0]:rows[1] for rows in reader}

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

lbl2_C = tk.Label(win, text="暗号 ➡ 言語", bg="black",fg="Green")
lbl2_C.pack()

input_C = tk.Entry(win, bg="#000", fg="Green", font=font3)
input_C.pack()

enterButton_C = tk.Button(win, text=' OK ', command=convert_CtoL ,bg="black" ,fg="Green")
enterButton_C.pack()

resultTitle_C = tk.Label(win, text="---------------------------- Result ----------------------------", fg="Green",bg="black", font=font2, height=2)
resultTitle_C.pack(side="top")

lbl3_C = tk.Text(win, width=40, height=4, bg="#000", fg="Green")
lbl3_C.pack()

copy_Button = tk.Button(text=" copy ", command=copyText, bg="black" ,fg="Green")
copy_Button.pack()


win.mainloop()