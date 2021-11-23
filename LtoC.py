import tkinter as tk
import csv
from tkinter import font

win = tk.Tk()
win.title("AnGO -L to C -")
win.geometry("400x300")
win.configure(bg="black")

def changeApp_CtoL():
    def return_view():
        win.destroy()

    win.geometry("400x300")
    win.title(u"AnGO -C to L-")
    # GUIデザイン-CtoL-
    lbl_C = tk.Label(win, text="AnGO", fg="Green", bg="black", font=font1, height=2)
    lbl_C.pack(side="top")

    lbl2_C = tk.Label(win, text="暗号 ➡ 言語", bg="black",fg="Green")
    lbl2_C.pack()

    input_C = tk.Entry(win, bg="#000", fg="Green", font=font3)
    input_C.pack()

    enterButton_C = tk.Button(win, text=' OK ', command=convert_CtoL ,bg="black" ,fg="Green")
    enterButton_C.pack()

    resultTitle_C = tk.Label(win, text="---------------------------- Result ----------------------------", fg="Green",bg="black", font=font2, height=5)
    resultTitle_C.pack(side="top")

    lbl3_C = tk.Label(win, text="---", fg="Green", bg="black")
    lbl3_C.pack()
    

def convert_LtoC():
    crypto = input_L.get()
    for word, read in LtoC_first.items():
      crypto = crypto.replace(word, read)
      print(crypto)
    
    Fcrypto = "　"+crypto
    lbl3_L.insert('1.0',Fcrypto)
    print(Fcrypto)

def convert_CtoL():
    crypto = input_C.get()
    for word, read in CtoL_first.items():
      crypto = crypto.replace(word, read)
      print(crypto)
    
    Fcrypto = crypto
    lbl3_C["text"] = Fcrypto
    print(Fcrypto)

# CSV読み込み処理
with open('LtoC_first.csv', mode='r') as inp:
    reader = csv.reader(inp)
    LtoC_first = {rows[0]:rows[1] for rows in reader}

with open('CtoL_first.csv', mode='r') as inp:
    reader = csv.reader(inp)
    CtoL_first = {rows[0]:rows[1] for rows in reader}

# フォント設定
font1 = font.Font(family='Helvetica', size=20, weight='bold')
font2 = font.Font(family='Helvetica', size=12, weight="bold")
font3 = font.Font(size=10)

# 変数定義
input_C=""
lbl3_C = " --- "
crypto = ""
Fcrypto = ""

# GUIデザイン-LtoC-
lbl_L = tk.Label(win, text="AnGO", fg="Green", bg="black", font=font1, height=2)
lbl_L.pack(side="top")

lbl2_L = tk.Label(win, text="言語 ➡ 暗号", bg="black",fg="Green")
lbl2_L.pack()

changeApp_Button_L = tk.Button(win, text=' 暗号➡言語 ',bg="black",fg="Green", command=changeApp_CtoL)
changeApp_Button_L.pack()

input_L = tk.Entry(win, bg="#000", fg="Green", font=font3)
input_L.pack()

enterButton_L = tk.Button(win, text=' OK ', command=convert_LtoC ,bg="black" ,fg="Green")
enterButton_L.pack()

resultTitle_L = tk.Label(win, text="---------------------------- Result ----------------------------", fg="Green",bg="black", font=font2, height=5)
resultTitle_L.pack(side="top")

lbl3_L = tk.Text(win, width=40, height=4, bg="#000", fg="Green")
lbl3_L.pack()

win.mainloop()