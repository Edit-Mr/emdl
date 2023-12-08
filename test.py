import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

frame = tk.Frame(root, width=15)        # 建立 Frame
frame.pack()

scrollbar = tk.Scrollbar(frame)         # 將 Frame 裡放入 Scrollbar
scrollbar.pack(side='right', fill='y')  # 設定位置在右側，垂直填滿

menu = tk.StringVar()
menu.set(('Apple','Banana','Orange','Grap','Papaya','Coconut','Pear','Nuts'))
# 在 Frame 中加入 Listbox 元件，設定 yscrollcommand=scrollbar.set
listbox = tk.Listbox(frame,  listvariable=menu, height=6, width=15, yscrollcommand=scrollbar.set)
listbox.pack(side='left', fill='y')    # 設定 Listbox 的位置以及填滿方式

scrollbar.config(command = listbox.yview)  # 設定 scrollbar 的 command = listbox.yview

root.mainloop()