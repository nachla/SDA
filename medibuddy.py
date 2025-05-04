# DEF FINAL===============================================================
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
from fpdf import FPDF
from datetime import datetime
import csv
import queue
import json
from tkcalendar import Calendar
import pandas as pd
from fpdf import FPDF
from gtts import gTTS
import pygame

# ===============================================HALAMAN TAMBAH BPJS===============================================
def tambahdatabpjs_page():
    global tambahbpjs
    tambahbpjs = tk.Toplevel(login)
    tambahbpjs.title("Tambah Data BPJS")
    width, height = tambahbpjs.winfo_screenwidth(), tambahbpjs.winfo_screenheight()
    tambahbpjs.geometry(f"{width}x{height}")

    bgtmbhbpjs1 = "bg tambah data bpjs.png"
    bgtmbhbpjs2 = Image.open(bgtmbhbpjs1)
    bgtmbhbpjs3 = bgtmbhbpjs2.resize((1550, 930))
    bgtmbhbpjs4 = ImageTk.PhotoImage(bgtmbhbpjs3)
    bgtmbhbpjs5 = tk.Label(tambahbpjs, image=bgtmbhbpjs4, bd=0)
    bgtmbhbpjs5.place(x=0, y=0)
    
    # =====
    entry_nama_bpjs = tk.Entry(tambahbpjs, width=29, fg='#1F4C73', border=0, bg='white', font=('Bahnschrift', 17))
    entry_nama_bpjs.place(x=415, y=465)

    entry_id_bpjs = tk.Entry(tambahbpjs, width=29, fg='#1F4C73', border=0, bg='white', font=('Bahnschrift', 17))
    entry_id_bpjs.place(x=415, y=578)

    entry_umur_bpjs = tk.Entry(tambahbpjs, width=29, fg='#1F4C73', border=0, bg='white', font=('Bahnschrift', 17))
    entry_umur_bpjs.place(x=415, y=685)

    # =====
    def tambah_data_bpjs():
        Nama = entry_nama_bpjs.get()
        Nomor_Kartu = entry_id_bpjs.get()
        Umur = entry_umur_bpjs.get()

        data = {'Nama': [Nama], 'Nomor Kartu BPJS': [Nomor_Kartu], 'Umur': [Umur]}
        df = pd.DataFrame(data)

        if not os.path.isfile('databpjs.csv'):
            df.to_csv('databpjs.csv', index=False)
            messagebox.showinfo('Info', 'Database berhasil dibuat dan data berhasil ditambahkan')
        else:
            if os.path.getsize('databpjs.csv') > 0:
                df.to_csv('databpjs.csv', mode='a', index=False, header=False)
                messagebox.showinfo('Info', 'Data berhasil ditambahkan ke Database')
            else:
                df.to_csv('databpjs.csv', index=False)
                messagebox.showinfo('Info', 'File databpjs.csv sudah ada, tetapi kosong. Data berhasil ditambahkan')
        tambahbpjs.withdraw()
        databpjs_page()

    btntmbhdt1 = "button tambah data.png"
    btntmbhdt2 = Image.open(btntmbhdt1)
    btntmbhdt3 = btntmbhdt2.resize((369, 55))
    btntmbhdt4 = ImageTk.PhotoImage(btntmbhdt3)
    btntmbhdt5 = tk.Button(tambahbpjs, image=btntmbhdt4, borderwidth=0, highlightthickness=0, relief=tk.FLAT, command=tambah_data_bpjs)
    btntmbhdt5.place(x=510, y=790)

    # =====
    def tambahbpjs_bpjs():
        tambahbpjs.destroy()
        bpjs.deiconify()

    btnbckbpjs1 = "button back.png"
    btnbckbpjs2 = Image.open(btnbckbpjs1)
    btnbckbpjs3 = btnbckbpjs2.resize((97, 55))
    btnbckbpjs4 = ImageTk.PhotoImage(btnbckbpjs3)
    btnbckbpjs5 = tk.Button(tambahbpjs, image=btnbckbpjs4, borderwidth=0, highlightthickness=0, relief=tk.FLAT, command=tambahbpjs_bpjs)
    btnbckbpjs5.place(x=403, y=790)

    cbbtnsdb1 = "button data bpjs side.png"
    cbbtnsdb2 = Image.open(cbbtnsdb1)
    cbbtnsdb3 = cbbtnsdb2.resize((100, 18))
    cbbtnsdb4 = ImageTk.PhotoImage(cbbtnsdb3)
    cbbtnsdb5 = tk.Button(tambahbpjs, image=cbbtnsdb4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_bpjs)
    cbbtnsdb5.place(x=100, y=263)

    # =====
    def tambahbpjs_dashboard():
        tambahbpjs.withdraw()
        dashboard.deiconify()

    cbbtnsda1 = "button beranda side.png"
    cbbtnsda2 = Image.open(cbbtnsda1)
    cbbtnsda3 = cbbtnsda2.resize((100, 18))
    cbbtnsda4 = ImageTk.PhotoImage(cbbtnsda3)
    cbbtnsda5 = tk.Button(tambahbpjs, image=cbbtnsda4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_dashboard)
    cbbtnsda5.place(x=100, y=189)

    # ====
    def tambahbpjs_pelayanan():
        tambahbpjs.withdraw()
        pelayanan.deiconify()
    cbbtnsdc1 = "button pelayanan side.png"
    cbbtnsdc2 = Image.open(cbbtnsdc1)
    cbbtnsdc3 = cbbtnsdc2.resize((110, 25))
    cbbtnsdc4 = ImageTk.PhotoImage(cbbtnsdc3)
    cbbtnsdc5 = tk.Button(tambahbpjs, image=cbbtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_pelayanan)
    cbbtnsdc5.place(x=100, y=338)

    # ====
    def tambahbpjs_antrian():
        tambahbpjs.withdraw()
        antrian.deiconify()
    cbbtnsdd1 = "button antrian side.png"
    cbbtnsdd2 = Image.open(cbbtnsdd1)
    cbbtnsdd3 = cbbtnsdd2.resize((95, 18))
    cbbtnsdd4 = ImageTk.PhotoImage(cbbtnsdd3)
    cbbtnsdd5 = tk.Button(tambahbpjs, image=cbbtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_antrian)
    cbbtnsdd5.place(x=100, y=419)

    # ====
    def tambahbpjs_dokter():
        tambahbpjs.withdraw()
        dokter.deiconify()
    cbbtnsde1 = "button dokter side.png"
    cbbtnsde2 = Image.open(cbbtnsde1)
    cbbtnsde3 = cbbtnsde2.resize((95, 18))
    cbbtnsde4 = ImageTk.PhotoImage(cbbtnsde3)
    cbbtnsde5 = tk.Button(tambahbpjs, image=cbbtnsde4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_dokter)
    cbbtnsde5.place(x=100, y=497)

    # ====
    def tambahbpjs_apoteker():
        tambahbpjs.withdraw()
        apoteker.deiconify()
    cbbtnsdf1 = "button apoteker side.png"
    cbbtnsdf2 = Image.open(cbbtnsdf1)
    cbbtnsdf3 = cbbtnsdf2.resize((100, 25))
    cbbtnsdf4 = ImageTk.PhotoImage(cbbtnsdf3)
    cbbtnsdf5 = tk.Button(tambahbpjs, image=cbbtnsdf4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_apoteker)
    cbbtnsdf5.place(x=100, y=572)

    # ====
    def tambahbpjs_login():
        tambahbpjs.withdraw()
        login.deiconify()
    cbbtnsdg1 = "button keluar side.png"
    cbbtnsdg2 = Image.open(cbbtnsdg1)
    cbbtnsdg3 = cbbtnsdg2.resize((90, 18))
    cbbtnsdg4 = ImageTk.PhotoImage(cbbtnsdg3)
    cbbtnsdg5 = tk.Button(tambahbpjs, image=cbbtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tambahbpjs_login)
    cbbtnsdg5.place(x=100, y=652)

    # =====
    label_time = tk.Label(tambahbpjs, border=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    label_date = tk.Label(tambahbpjs, border=0, font=('Century Gothic Bold', 17))
    label_date.place(x=150, y=862, anchor="center")
    label_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        tambahbpjs.after(1000, update_time_date)  
    update_time_date()

    tambahbpjs.mainloop()
# ===============================================HALAMAN DATA BPJS====================================================
def databpjs_page():
    global dashboard, bpjs, tambahbpjs
    bpjs=tk.Toplevel(login)
    bpjs.title("Data BPJS")
    width, height = bpjs.winfo_screenwidth(), bpjs.winfo_screenheight()
    bpjs.geometry(f"{width}x{height}")
    bpjs.configure(bg="#C8E8F5")
    bpjs.resizable(False, False)

    bgbpjs1 = "bg data bpjs.png"
    bgbpjs2 = Image.open(bgbpjs1)
    bgbpjs3 = bgbpjs2.resize((1550, 930))
    bgbpjs4 = ImageTk.PhotoImage(bgbpjs3)
    bgbpjs5 = tk.Label(bpjs, image=bgbpjs4, bd=0)
    bgbpjs5.place(x=0, y=0)

# =======================================================tabel
    def tampilkan_data_bpjs(sort_func=None):
        global tree
        # Baca file CSV
        df = pd.read_csv('databpjs.csv')

        # Urutkan data jika fungsi sort disediakan
        if sort_func:
            df = sort_func(df, 'Nama')

        # Hapus Treeview yang ada jika ada
        for widget in bpjs.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=53, font=('Century Gothic', 13, "bold"))  # Font baris
        style.configure("Treeview.Heading", font=('Helvetica', 16))  # Font judul
        style.map("Treeview", foreground=[
            ('!selected', '#4E7CA0'),
            ('selected', '#FFFFFF'),   
            ('active', '#4E7CA0')])
        
        columns = ('nama', 'id', 'umur')
        tree = ttk.Treeview(bpjs, columns=columns, show='headings', style="Treeview")
        tree.heading('nama', text='Nama')
        tree.heading('id', text='Nomor ID BPJS')
        tree.heading('umur', text='Umur')
        tree.column('nama', width=330, anchor='center')
        tree.column('id', width=330, anchor='center')
        tree.column('umur', width=330, anchor='center')
        tree.place(x=350, y=300)

        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))
    tampilkan_data_bpjs()

                   #[[[[[[[[[[[[[[[[[[[[[[[[[[[[  S O R T I N G  ]]]]]]]]]]]]]]]]]]]]]]]]]]]]

    def quick_sort_az(df, col_name):
        if len(df) <= 1:
            return df
        else:
            pivot = df[col_name].iloc[0]
            less_than_pivot = df[df[col_name] < pivot]
            equal_to_pivot = df[df[col_name] == pivot]
            greater_than_pivot = df[df[col_name] > pivot]
            return pd.concat([quick_sort_az(less_than_pivot, col_name), equal_to_pivot, quick_sort_az(greater_than_pivot, col_name)])
        
    def quick_sort_za(df, col_name):
        if len(df) <= 1:
            return df
        else:
            pivot = df[col_name].iloc[0]
            less_than_pivot = df[df[col_name] > pivot]
            equal_to_pivot = df[df[col_name] == pivot]
            greater_than_pivot = df[df[col_name] < pivot]
            return pd.concat([quick_sort_za(less_than_pivot, col_name), equal_to_pivot, quick_sort_za(greater_than_pivot, col_name)])
        
    def quick_sort_kartu_terkecil(df, col_name):
        if len(df) <= 1:
            return df
        else:
            pivot = df[col_name].iloc[0]
            less_than_pivot = df[df[col_name] < pivot]
            equal_to_pivot = df[df[col_name] == pivot]
            greater_than_pivot = df[df[col_name] > pivot]
            return pd.concat([quick_sort_kartu_terkecil(less_than_pivot, col_name), equal_to_pivot, quick_sort_kartu_terkecil(greater_than_pivot, col_name)])
        
    def quick_sort_kartu_terbesar(df, col_name):
        if len(df) <= 1:
            return df
        else:
            pivot = df[col_name].iloc[0]
            less_than_pivot = df[df[col_name] > pivot]
            equal_to_pivot = df[df[col_name] == pivot]
            greater_than_pivot = df[df[col_name] < pivot]
            return pd.concat([quick_sort_kartu_terbesar(less_than_pivot, col_name), equal_to_pivot, quick_sort_kartu_terbesar(greater_than_pivot, col_name)])
        
    def quick_sort_umur_termuda(df, col_name):
        if len(df) <= 1:
            return df
        else:
            pivot = df[col_name].iloc[0]
            less_than_pivot = df[df[col_name] < pivot]
            equal_to_pivot = df[df[col_name] == pivot]
            greater_than_pivot = df[df[col_name] > pivot]
            return pd.concat([quick_sort_umur_termuda(less_than_pivot, col_name), equal_to_pivot, quick_sort_umur_termuda(greater_than_pivot, col_name)])
        
    def quick_sort_umur_tertua(df, col_name):
        if len(df) <= 1:
            return df
        else:
            pivot = df[col_name].iloc[0]
            less_than_pivot = df[df[col_name] > pivot]
            equal_to_pivot = df[df[col_name] == pivot]
            greater_than_pivot = df[df[col_name] < pivot]
            return pd.concat([quick_sort_umur_tertua(less_than_pivot, col_name), equal_to_pivot, quick_sort_umur_tertua(greater_than_pivot, col_name)])

    def tampilkan_data_bpjs_az():
        tampilkan_data_bpjs(quick_sort_az)
        
    def tampilkan_data_bpjs_za():
        tampilkan_data_bpjs(quick_sort_za)
        
    def tampilkan_data_bpjs_kartu_terkecil():
        tampilkan_data_bpjs(lambda df, _: quick_sort_kartu_terkecil(df, 'Nomor Id BPJS'))
        
    def tampilkan_data_bpjs_kartu_terbesar():
        tampilkan_data_bpjs(lambda df, _: quick_sort_kartu_terbesar(df, 'Nomor Id BPJS'))
        
    def tampilkan_data_bpjs_umur_termuda():
        tampilkan_data_bpjs(lambda df, _: quick_sort_umur_termuda(df, 'Umur'))
        
    def tampilkan_data_bpjs_umur_tertua():
        tampilkan_data_bpjs(lambda df, _: quick_sort_umur_tertua(df, 'Umur'))

    btnsrtaz1 = "button sorting az.png"
    btnsrtaz2 = Image.open(btnsrtaz1)
    btnsrtaz3 = btnsrtaz2.resize((100, 30))
    btnsrtaz4 = ImageTk.PhotoImage(btnsrtaz3)
    btnsrtaz5 = tk.Button(bpjs, image=btnsrtaz4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=tampilkan_data_bpjs_az)
    btnsrtaz5.place(x=698, y=168)

    btnsrtza1 = "button sorting za.png"
    btnsrtza2 = Image.open(btnsrtza1)
    btnsrtza3 = btnsrtza2.resize((100, 30))
    btnsrtza4 = ImageTk.PhotoImage(btnsrtza3)
    btnsrtza5 = tk.Button(bpjs, image=btnsrtza4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=tampilkan_data_bpjs_za)
    btnsrtza5.place(x=698, y=211)

    btnsrtkcl1 = "button sorting id terkecil.png"
    btnsrtkcl2 = Image.open(btnsrtkcl1)
    btnsrtkcl3 = btnsrtkcl2.resize((165, 30))
    btnsrtkcl4 = ImageTk.PhotoImage(btnsrtkcl3)
    btnsrtkcl5 = tk.Button(bpjs, image=btnsrtkcl4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=tampilkan_data_bpjs_kartu_terkecil)
    btnsrtkcl5.place(x=805, y=167)

    btnsrtbsr1 = "button sorting id terbesar.png"
    btnsrtbsr2 = Image.open(btnsrtbsr1)
    btnsrtbsr3 = btnsrtbsr2.resize((165, 30))
    btnsrtbsr4 = ImageTk.PhotoImage(btnsrtbsr3)
    btnsrtbsr5 = tk.Button(bpjs, image=btnsrtbsr4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=tampilkan_data_bpjs_kartu_terbesar)
    btnsrtbsr5.place(x=805, y=211)

    btnsrtmda1 = "button sorting termuda.png"
    btnsrtmda2 = Image.open(btnsrtmda1)
    btnsrtmda3 = btnsrtmda2.resize((148, 30))
    btnsrtmda4 = ImageTk.PhotoImage(btnsrtmda3)
    btnsrtmda5 = tk.Button(bpjs, image=btnsrtmda4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=tampilkan_data_bpjs_umur_termuda)
    btnsrtmda5.place(x=977, y=167)

    btnsrttua1 = "button sorting tertua.png"
    btnsrttua2 = Image.open(btnsrttua1)
    btnsrttua3 = btnsrttua2.resize((148, 30))
    btnsrttua4 = ImageTk.PhotoImage(btnsrttua3)
    btnsrttua5 = tk.Button(bpjs, image=btnsrttua4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=tampilkan_data_bpjs_umur_tertua)
    btnsrttua5.place(x=977, y=211)

    # =====
    def hapus_data_bpjs():
        selected_item = tree.selection()  # Mendapatkan item yang dipilih
        if not selected_item:
            messagebox.showwarning('Invalid', 'Pilih data yang akan dihapus')
            return

        item = tree.item(selected_item)
        item_values = item['values'] #ambil nilai
        tree.delete(selected_item) #hapus dri tabel

        # hapus dari csv
        df = pd.read_csv('databpjs.csv')
        df = df[~((df['Nama'] == item_values[0]) & (df['Nomor Id BPJS'] == item_values[1]) & (df['Umur'] == item_values[2]))]
        df.to_csv('databpjs.csv', index=False)
        messagebox.showinfo('Info', 'Data berhasil dihapus')

    btnhps1 = "button hapus.png"
    btnhps2 = Image.open(btnhps1)
    btnhps3 = btnhps2.resize((160, 70))
    btnhps4 = ImageTk.PhotoImage(btnhps3)
    btnhps5 = tk.Button(bpjs, image=btnhps4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=hapus_data_bpjs)
    btnhps5.place(x=1345, y=172)

    # =====
    def bpjs_tambahbpjs():
        bpjs.withdraw()
        tambahdatabpjs_page()

    btntmbh1 = "button tambah.png"
    btntmbh2 = Image.open(btntmbh1)
    btntmbh3 = btntmbh2.resize((160, 70))
    btntmbh4 = ImageTk.PhotoImage(btntmbh3)
    btntmbh5 = tk.Button(bpjs, image=btntmbh4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_tambahbpjs)
    btntmbh5.place(x=1175, y=172)

    # =====
    def bpjs_dashboard():
        bpjs.destroy()
        dashboard_page()

    bbtnsda1 = "button beranda side.png"
    bbtnsda2 = Image.open(bbtnsda1)
    bbtnsda3 = bbtnsda2.resize((100, 18))
    bbtnsda4 = ImageTk.PhotoImage(bbtnsda3)
    bbtnsda5 = tk.Button(bpjs, image=bbtnsda4, borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_dashboard)
    bbtnsda5.place(x=100, y=189)

    # =====
    bbtnsdb1 = "button data bpjs side.png"
    bbtnsdb2 = Image.open(bbtnsdb1)
    bbtnsdb3 = bbtnsdb2.resize((100, 18))
    bbtnsdb4 = ImageTk.PhotoImage(bbtnsdb3)
    bbtnsdb5 = tk.Button(bpjs, image=bbtnsdb4, borderwidth=0, highlightthickness=0, relief=FLAT)
    bbtnsdb5.place(x=100, y=263)

    # =====
    def bpjs_pelayanan():
        bpjs.destroy()
        pelayanan.deiconify()
    bbtnsdc1 = "button pelayanan side.png"
    bbtnsdc2 = Image.open(bbtnsdc1)
    bbtnsdc3 = bbtnsdc2.resize((110, 25))
    bbtnsdc4 = ImageTk.PhotoImage(bbtnsdc3)
    bbtnsdc5 = tk.Button(bpjs, image=bbtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_pelayanan)
    bbtnsdc5.place(x=100, y=338)
    # ====
    def bpjs_antrian():
        bpjs.destroy()
        antrian.deiconify()
    bbtnsdd1 = "button antrian side.png"
    bbtnsdd2 = Image.open(bbtnsdd1)
    bbtnsdd3 = bbtnsdd2.resize((95, 18))
    bbtnsdd4 = ImageTk.PhotoImage(bbtnsdd3)
    bbtnsdd5 = tk.Button(bpjs, image=bbtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_antrian)
    bbtnsdd5.place(x=100, y=419)

    # ====
    def bpjs_dokter():
        bpjs.destroy()
        dokter.deiconify()
    bbtnsde1 = "button dokter side.png"
    bbtnsde2 = Image.open(bbtnsde1)
    bbtnsde3 = bbtnsde2.resize((95, 18))
    bbtnsde4 = ImageTk.PhotoImage(bbtnsde3)
    bbtnsde5 = tk.Button(bpjs, image=bbtnsde4, borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_dokter)
    bbtnsde5.place(x=100, y=497)

    # ====
    def bpjs_apoteker():
        bpjs.withdraw()
        apoteker.deiconify()
    bbtnsdf1 = "button apoteker side.png"
    bbtnsdf2 = Image.open(bbtnsdf1)
    bbtnsdf3 = bbtnsdf2.resize((100, 25))
    bbtnsdf4 = ImageTk.PhotoImage(bbtnsdf3)
    bbtnsdf5 = tk.Button(bpjs, image=bbtnsdf4, borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_apoteker)
    bbtnsdf5.place(x=100, y=572)

    # ====
    def bpjs_login():
        bpjs.destroy()
        login.deiconify()
    bbtnsdg1 = "button keluar side.png"
    bbtnsdg2 = Image.open(bbtnsdg1)
    bbtnsdg3 = bbtnsdg2.resize((90, 18))
    bbtnsdg4 = ImageTk.PhotoImage(bbtnsdg3)
    bbtnsdg5 = tk.Button(bpjs, image=bbtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=bpjs_login)
    bbtnsdg5.place(x=100, y=652)
    # ====
    label_time = tk.Label(bpjs, border=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    label_date = tk.Label(bpjs, border=0, font=('Century Gothic Bold', 17))
    label_date.place(x=150, y=862, anchor="center")
    label_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        bpjs.after(1000, update_time_date) 
    update_time_date()

    bpjs.mainloop()

# ===============================================HALAMAN PELAYANAN======================================================================
def system_page():
    global pelayanan, antrian, dokter, apoteker
    pelayanan=tk.Toplevel(login)
    pelayanan.title("Pelayanan")
    width, height = pelayanan.winfo_screenwidth(), pelayanan.winfo_screenheight()
    pelayanan.geometry(f"{width}x{height}")
    pelayanan.configure(bg="#C8E8F5")
    pelayanan.resizable(False, False)

    bgplyn1 = "bg pelayanan.png"
    bgplyn2 = Image.open(bgplyn1)
    bgplyn3 = bgplyn2.resize((1550, 930))
    bgplyn4 = ImageTk.PhotoImage(bgplyn3)
    bgplyn5 = tk.Label(pelayanan, image=bgplyn4, bd=0)
    bgplyn5.place(x=0, y=0)

                   #[[[[[[[[[[[[  S E A R C H  ]]]]]]]]]]]]]]]

    searchentry = tk.Entry(pelayanan, width=28, border=0, font=('Century Gothic Bold',17))
    searchentry.place(x=493, y=340)

    stylea = ttk.Style()
    stylea.theme_use("clam")
    stylea.layout("TreeviewA", stylea.layout("Treeview"))
    stylea.configure("TreeviewA", rowheight=40, font=("Century Gothic", 13, "bold"))  #font baris
    stylea.configure("TreeviewA.Heading", background="#4F7CA1", foreground="white", font=("Century Gothic bold", 16)) #font judul
    stylea.map("TreeviewA", 
        foreground=[
        ('!selected', '#4E7CA0'), #warna huruf jika tidak dipilih
        ('selected', '#FFFFFF'), #warna huruf jika dipilih
        ('active', '#4E7CA0')], #warna huruf jika tidak dipilih
        background=[
        ('!selected', '#FFFFFF'), #warna bg jika tidak dipilih
        ('selected', '#4E7CA0')]) #warna bg jika tidak dipilih
    columns=("Nama", "Nomor Id BPJS", "Umur")
    search_table = ttk.Treeview(pelayanan, columns=columns, show='headings', style="TreeviewA")
    search_table.heading("Nama", text="Nama")
    search_table.heading("Nomor Id BPJS", text="Nomor Id BPJS")
    search_table.heading("Umur", text="Umur")
    search_table.column('Nama', width=330, anchor='center')
    search_table.column('Nomor Id BPJS', width=330, anchor='center')
    search_table.column('Umur', width=330, anchor='center')
    search_table.place(x=350, y=400)

    def load_data(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    
    def display_data(data):
        for row in data:
            search_table.insert("", "end", values=(row['Nama'], row['Nomor Id BPJS'], row['Umur']))

    def clear_table():
        for item in search_table.get_children():
            search_table.delete(item)
    
    def binary_search(data, target, key):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid][key] == target:
                return mid
            elif data[mid][key] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


    def search():
        query = searchentry.get().strip()
        if not query:
            clear_table()
            return

        if query.isdigit():
            key = 'Nomor Id BPJS'
        else:
            key = 'Nama'

        data = load_data('databpjs.csv')
        results = [entry for entry in data if query.lower() in str(entry[key]).lower()]
        clear_table()
        if results:
            display_data(results)
        else:
            messagebox.showwarning("Invalid", "Data tidak ada")

    btnsrch1 = "button search.png"
    btnsrch2 = Image.open(btnsrch1)
    btnsrch3 = btnsrch2.resize((100, 65))
    btnsrch4 = ImageTk.PhotoImage(btnsrch3)
    btnsrch5 = tk.Button(pelayanan, image=btnsrch4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=search)
    btnsrch5.place(x=975, y=325)

                #[[[[[[[[[[[[  P R I O R I T Y  Q U E U E  ]]]]]]]]]]]]]]]]]]]]

    priority_queue = queue.PriorityQueue()

    def clear_queue_table():
        if queue_table is not None:
            for item in queue_table.get_children():
                queue_table.delete(item)

    def display_queue_data():
        clear_queue_table()
        for item in sorted(priority_queue.queue, key=lambda x: x[0]):
            queue_table.insert("", "end", values=(item[2]['Nama'], item[2]['Nomor Id BPJS'], item[2]['Umur'], item[0]))

    def add_to_queue(priority):
        selected_item = search_table.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Pilih data pasien terlebih dahulu")
            return
        item_values = search_table.item(selected_item, 'values')
        item = {'Nama': item_values[0], 
                'Nomor Id BPJS': item_values[1], 
                'Umur': item_values[2],
                'priority': priority,
                'Time': datetime.now()}
        priority_queue.put((priority, item['Time'], item))  # Menambahkan timestamp ke dalam tuple
        display_queue_data()
        messagebox.showinfo("Info", "Berhasil ditambahkan ke antrian")

    btnpsatu1 = "button prioritas 1.png"
    btnpsatu2 = Image.open(btnpsatu1)
    btnpsatu3 = btnpsatu2.resize((210, 60))
    btnpsatu4 = ImageTk.PhotoImage(btnpsatu3)
    btnpsatu5 = tk.Button(pelayanan, image=btnpsatu4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=lambda: add_to_queue(1))
    btnpsatu5.place(x=800, y=175)

    btnpdua1 = "button prioritas 2.png"
    btnpdua2 = Image.open(btnpdua1)
    btnpdua3 = btnpdua2.resize((210, 60))
    btnpdua4 = ImageTk.PhotoImage(btnpdua3)
    btnpdua5 = tk.Button(pelayanan, image=btnpdua4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=lambda: add_to_queue(2))
    btnpdua5.place(x=1019, y=175)

    btntprio1 = "button tanpa prioritas.png"
    btntprio2 = Image.open(btntprio1)
    btntprio3 = btntprio2.resize((270, 60))
    btntprio4 = ImageTk.PhotoImage(btntprio3)
    btntprio5 = tk.Button(pelayanan, image=btntprio4, bg="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=lambda: add_to_queue(3))
    btntprio5.place(x=1237, y=175)

    # ======
    def pelayanan_dashboard():
        pelayanan.withdraw()
        dashboard.deiconify()
    dcbbtnsda1 = "button beranda side.png"
    dcbbtnsda2 = Image.open(dcbbtnsda1)
    dcbbtnsda3 = dcbbtnsda2.resize((100, 18))
    dcbbtnsda4 = ImageTk.PhotoImage(dcbbtnsda3)
    dcbbtnsda5 = tk.Button(pelayanan, image=dcbbtnsda4, borderwidth=0, highlightthickness=0, relief=FLAT, command=pelayanan_dashboard)
    dcbbtnsda5.place(x=100, y=189)
    # ====
    def pelayanan_bpjs():
        pelayanan.withdraw()
        databpjs_page()
    dcbbtnsdb1 = "button data bpjs side.png"
    dcbbtnsdb2 = Image.open(dcbbtnsdb1)
    dcbbtnsdb3 = dcbbtnsdb2.resize((100, 18))
    dcbbtnsdb4 = ImageTk.PhotoImage(dcbbtnsdb3)
    dcbbtnsdb5 = tk.Button(pelayanan, image=dcbbtnsdb4, borderwidth=0, highlightthickness=0, relief=FLAT, command=pelayanan_bpjs)
    dcbbtnsdb5.place(x=100, y=263)
    # ====
    dcbbtnsdc1 = "button pelayanan side.png"
    dcbbtnsdc2 = Image.open(dcbbtnsdc1)
    dcbbtnsdc3 = dcbbtnsdc2.resize((110, 25))
    dcbbtnsdc4 = ImageTk.PhotoImage(dcbbtnsdc3)
    dcbbtnsdc5 = tk.Button(pelayanan, image=dcbbtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT)
    dcbbtnsdc5.place(x=100, y=338)

    # ====
    def pelayanan_antrian():
        pelayanan.withdraw()
        antrian.deiconify()
    dcbbtnsdd1 = "button antrian side.png"
    dcbbtnsdd2 = Image.open(dcbbtnsdd1)
    dcbbtnsdd3 = dcbbtnsdd2.resize((95, 18))
    dcbbtnsdd4 = ImageTk.PhotoImage(dcbbtnsdd3)
    dcbbtnsdd5 = tk.Button(pelayanan, image=dcbbtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=pelayanan_antrian)
    dcbbtnsdd5.place(x=100, y=419)


    # ====
    def pelayanan_dokter():
        pelayanan.withdraw()
        dokter.deiconify()
    dcbbtnsde1 = "button dokter side.png"
    dcbbtnsde2 = Image.open(dcbbtnsde1)
    dcbbtnsde3 = dcbbtnsde2.resize((95, 18))
    dcbbtnsde4 = ImageTk.PhotoImage(dcbbtnsde3)
    dcbbtnsde5 = tk.Button(pelayanan, image=dcbbtnsde4, borderwidth=0, highlightthickness=0, relief=FLAT, command=pelayanan_dokter)
    dcbbtnsde5.place(x=100, y=497)


    # ====
    def pelayanan_apoteker():
        pelayanan.withdraw()
        apoteker.deiconify()
    dcbbtnsdf1 = "button apoteker side.png"
    dcbbtnsdf2 = Image.open(dcbbtnsdf1)
    dcbbtnsdf3 = dcbbtnsdf2.resize((100, 25))
    dcbbtnsdf4 = ImageTk.PhotoImage(dcbbtnsdf3)
    dcbbtnsdf5 = tk.Button(pelayanan, image=dcbbtnsdf4, borderwidth=0, highlightthickness=0, relief=FLAT, command=pelayanan_apoteker)
    dcbbtnsdf5.place(x=100, y=572)

    # ====
    def pelayanan_login():
        pelayanan.withdraw()
        login.deiconify()
    dcbbtnsdg1 = "button keluar side.png"
    dcbbtnsdg2 = Image.open(dcbbtnsdg1)
    dcbbtnsdg3 = dcbbtnsdg2.resize((90, 18))
    dcbbtnsdg4 = ImageTk.PhotoImage(dcbbtnsdg3)
    dcbbtnsdg5 = tk.Button(pelayanan, image=dcbbtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=pelayanan_login)
    dcbbtnsdg5.place(x=100, y=652)

    # ======
    label_time = tk.Label(pelayanan, border=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    label_date = tk.Label(pelayanan, border=0, font=('Century Gothic Bold', 17))
    label_date.place(x=150, y=862, anchor="center")
    label_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        pelayanan.after(1000, update_time_date)  
    update_time_date()

# ===============================================HALAMAN ANTRIAN===========================================
    antrian=tk.Toplevel(pelayanan)
    antrian.title("Antrian")
    width, height = antrian.winfo_screenwidth(), antrian.winfo_screenheight()
    antrian.geometry(f"{width}x{height}")
    antrian.configure(bg="#C8E8F5")
    antrian.resizable(False, False)

    bgantrian1 = "bg antrian.png"
    bgantrian2 = Image.open(bgantrian1)
    bgantrian3 = bgantrian2.resize((1550, 930))
    bgantrian4 = ImageTk.PhotoImage(bgantrian3)
    bgantrian5 = tk.Label(antrian, image=bgantrian4, bd=0)
    bgantrian5.place(x=0, y=0)

    # hallostaf = Label(antrian, text=f"Hallo, {Namastaf}", font=('Century Gothic bold italic', 17), fg='#024480', bg='#FAFAFA')
    # hallostaf.place(x=1270, y=45, anchor='e')

    # ====
    styleo = ttk.Style()
    styleo.theme_use("clam")
    styleo.configure("Treeview", rowheight=53, font=("Century Gothic", 13, "bold"))  #font baris
    styleo.configure("Treeview.Heading", background="#4F7CA1",foreground="white",font=("Century Gothic bold", 16)) #font judul
    styleo.map("Treeview", foreground=[
        ('!selected', '#4E7CA0'),   
        ('selected', '#FFFFFF'),   
        ('active', '#4E7CA0')]) 
    columns = ('nama', 'id', 'umur', 'priority')
    queue_table = ttk.Treeview(antrian, columns=columns, show='headings', style="Treeview")
    queue_table.heading('nama', text='Nama')
    queue_table.heading('id', text='ID')
    queue_table.heading('umur', text='Umur')
    queue_table.heading('priority', text='Prioritas')
    queue_table.column('nama', width=325, anchor='center')
    queue_table.column('id', width=325, anchor='center')
    queue_table.column('umur', width=200, anchor='center')
    queue_table.column('priority', width=200, anchor='center')
    queue_table.place(x=350, y=300)

    # ====
    def antrian_dashboard():
        antrian.withdraw()
        dashboard.deiconify()
    edcbbtnsda1 = "button beranda side.png"
    edcbbtnsda2 = Image.open(edcbbtnsda1)
    edcbbtnsda3 = edcbbtnsda2.resize((100, 18))
    edcbbtnsda4 = ImageTk.PhotoImage(edcbbtnsda3)
    edcbbtnsda5 = tk.Button(antrian, image=edcbbtnsda4, borderwidth=0, highlightthickness=0, relief=FLAT, command=antrian_dashboard)
    edcbbtnsda5.place(x=100, y=189)

    # ====
    def antrian_bpjs():
        antrian.withdraw()
        databpjs_page()
    edcbbtnsdb1 = "button data bpjs side.png"
    edcbbtnsdb2 = Image.open(edcbbtnsdb1)
    edcbbtnsdb3 = edcbbtnsdb2.resize((100, 18))
    edcbbtnsdb4 = ImageTk.PhotoImage(edcbbtnsdb3)
    edcbbtnsdb5 = tk.Button(antrian, image=edcbbtnsdb4, borderwidth=0, highlightthickness=0, relief=FLAT, command=antrian_bpjs)
    edcbbtnsdb5.place(x=100, y=263)

    # ====
    def antrian_pelayanan():
        antrian.withdraw()
        pelayanan.deiconify()
    edcbbtnsdc1 = "button pelayanan side.png"
    edcbbtnsdc2 = Image.open(edcbbtnsdc1)
    edcbbtnsdc3 = edcbbtnsdc2.resize((110, 25))
    edcbbtnsdc4 = ImageTk.PhotoImage(edcbbtnsdc3)
    edcbbtnsdc5 = tk.Button(antrian, image=edcbbtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=antrian_pelayanan)
    edcbbtnsdc5.place(x=100, y=338)

    # ====
    edcbbtnsdd1 = "button antrian side.png"
    edcbbtnsdd2 = Image.open(edcbbtnsdd1)
    edcbbtnsdd3 = edcbbtnsdd2.resize((95, 18))
    edcbbtnsdd4 = ImageTk.PhotoImage(edcbbtnsdd3)
    edcbbtnsdd5 = tk.Button(antrian, image=edcbbtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT)
    edcbbtnsdd5.place(x=100, y=419)


    # =====
    def antrian_dokter():
        antrian.withdraw()
        dokter.deiconify()
    edcbbtnsde1 = "button dokter side.png"
    edcbbtnsde2 = Image.open(edcbbtnsde1)
    edcbbtnsde3 = edcbbtnsde2.resize((95, 18))
    edcbbtnsde4 = ImageTk.PhotoImage(edcbbtnsde3)
    edcbbtnsde5 = tk.Button(antrian, image=edcbbtnsde4, borderwidth=0, highlightthickness=0, relief=FLAT, command=antrian_dokter)
    edcbbtnsde5.place(x=100, y=497)


    # =====
    def antrian_apoteker():
        antrian.withdraw()
        apoteker.deiconify()
    edcbbtnsdf1 = "button apoteker side.png"
    edcbbtnsdf2 = Image.open(edcbbtnsdf1)
    edcbbtnsdf3 = edcbbtnsdf2.resize((100, 25))
    edcbbtnsdf4 = ImageTk.PhotoImage(edcbbtnsdf3)
    edcbbtnsdf5 = tk.Button(antrian, image=edcbbtnsdf4, borderwidth=0, highlightthickness=0, relief=FLAT, command=antrian_apoteker)
    edcbbtnsdf5.place(x=100, y=572)

    # ====
    def antrian_login():
        antrian.withdraw()
        login.deiconify()
    edcbbtnsdg1 = "button keluar side.png"
    edcbbtnsdg2 = Image.open(edcbbtnsdg1)
    edcbbtnsdg3 = edcbbtnsdg2.resize((90, 18))
    edcbbtnsdg4 = ImageTk.PhotoImage(edcbbtnsdg3)
    edcbbtnsdg5 = tk.Button(antrian, image=edcbbtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=antrian_login)
    edcbbtnsdg5.place(x=100, y=652)

    # ====
    label_time = tk.Label(antrian, border=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    label_date = tk.Label(antrian, border=0, font=('Century Gothic Bold', 17))
    label_date.place(x=150, y=6862, anchor="center")
    label_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        antrian.after(1000, update_time_date)  
    update_time_date()

# =========================================================HALAMAN DOKTER==============================================
    dokter = tk.Toplevel(pelayanan)
    dokter.title("Dokter")
    width, height = dokter.winfo_screenwidth(), dokter.winfo_screenheight()
    dokter.geometry(f"{width}x{height}")
    dokter.configure(bg="#C8E8F5")
    dokter.resizable(False, False)

    bgdokter1 = "bg dokter.png"
    bgdokter2 = Image.open(bgdokter1)
    bgdokter3 = bgdokter2.resize((1550, 930))
    bgdokter4 = ImageTk.PhotoImage(bgdokter3)
    bgdokter5 = tk.Label(dokter, image=bgdokter4, bd=0)
    bgdokter5.place(x=0, y=0)

    # hallostaf = Label(dokter, text=f"Hallo, {Namastaf}", font=('Century Gothic bold italic', 17), fg='#024480', bg='#FAFAFA')
    # hallostaf.place(x=1270, y=45, anchor='e')

    # ====
    nmpasiendktr = tk.Label(dokter, text="", bg="white")
    nmpasiendktr.place(x=495, y=387)

    bpjspasiendktr = tk.Label(dokter, text="", bg="white")
    bpjspasiendktr.place(x=495, y=420)

    umrpasiendktr = tk.Label(dokter, text="", bg="white")
    umrpasiendktr.place(x=495, y=452)
 
    tgientry = Text(dokter, width=5, height=1, bd=2, font=('Bahnschrift',14), relief=FLAT)
    tgientry.place(x=495, y=486)

    brtentry = Text(dokter, width=5, height=1, bd=2, font=('Bahnschrift',14), relief=FLAT)
    brtentry.place(x=495, y=516)

    iddokterentry= Text(dokter, width=13, height=1, bd=2, font=('Bahnschrift',11), relief=FLAT)
    iddokterentry.place(x=1060, y=213)

    keluhanentry = Text(dokter, width=40, height=8, bd=2, font=20, relief=FLAT)
    keluhanentry.place(x=382, y=650)

    resepentry = Text(dokter, width=47, height=15, bd=2, font=20, relief=FLAT)
    resepentry.place(x=945, y=395)

    # ====
    def update_patient_data(patient):
        global nmpasienout, idpasienout, umrpasienout

        nmpasiendktr.config(text=f"{patient['Nama']}", bg="white", font=('Bahnschrift',14))
        bpjspasiendktr.config(text=f"{patient['Nomor Id BPJS']}", bg="white", font=('Bahnschrift',14))
        umrpasiendktr.config(text=f"{patient['Umur']}", bg="white", font=('Bahnschrift',14))

        nmpasienout = tk.Label(apoteker, text=f"{patient['Nama']}", bg="white", font=('Bahnschrift',14))
        nmpasienout.place(x=1135, y=380)
        idpasienout = tk.Label(apoteker, text=f"{patient['Nomor Id BPJS']}", bg="white", font=('Bahnschrift',14))
        idpasienout.place(x=1135, y=412)
        umrpasienout = tk.Label(apoteker, text=f"{patient['Umur']}", bg="white", font=('Bahnschrift',14))
        umrpasienout.place(x=1135, y=442)

        
    def speak_patient_name(name):
        tts = gTTS(text=f"Pasien dengan nama {name}, silahkan segera ke ruang dokter.   Pasien dengan nama {name}, silahkan segera ke ruang dokter.", lang='id')
        tts.save("call.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("call.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()
        os.remove("call.mp3")

    def call_patient():
        if not priority_queue.empty():
            _, _, patient = priority_queue.get()
            update_patient_data(patient)
            speak_patient_name(patient['Nama'])
            display_queue_data()
        else:
            messagebox.showwarning("Error", "Tidak ada pasien dalam antrian")

    btnpgl1 = "button panggil.png"
    btnpgl2 = Image.open(btnpgl1)
    btnpgl3 = btnpgl2.resize((225, 57))
    btnpgl4 = ImageTk.PhotoImage(btnpgl3)
    btnpgl5 = tk.Button(dokter, image=btnpgl4, background="white", relief=FLAT, command=call_patient)
    btnpgl5.place(x=1264, y=175)

    # ====
    def hapusentrydokter():
        tgientry.delete("1.0", tk.END)
        brtentry.delete("1.0", tk.END)
        keluhanentry.delete("1.0", tk.END)
        resepentry.delete("1.0", tk.END)

    def kirim():
        text = resepentry.get("1.0", END).strip()
        if text:
            lblresep.config(text=text)
            messagebox.showinfo("Info", "Resep telah dikirim ke Apoteker")
        else:
            messagebox.showwarning("Peringatan", "Entry tidak boleh kosong")


    btnkrm = "button kirim.png"
    btnkrm1 = Image.open(btnkrm)
    btnkrm2 = btnkrm1.resize((150, 65))
    btnkrm3 = ImageTk.PhotoImage(btnkrm2)
    btnkrm4 = tk.Button(dokter, image=btnkrm3 , background="white", relief=FLAT, command=kirim)
    btnkrm4.place(x=1330, y=805)

    # ====
    def satukali():
        txtsatu = " 1x Sehari "  
        resepentry.insert(tk.END, txtsatu)
    btnsatu1 = "button satu kali.png"
    btnsatu2 = Image.open(btnsatu1)
    btnsatu3 = btnsatu2.resize((122, 25))
    btnsatu4 = ImageTk.PhotoImage(btnsatu3)
    btnsatu5 = tk.Button(dokter, image=btnsatu4, background="white", relief=FLAT, command=satukali)
    btnsatu5.place(x=922, y=808)

    # ====
    def duakali():
        txtdua = " 2x Sehari "  
        resepentry.insert(tk.END, txtdua)
    btndua1 = "button dua kali.png"
    btndua2 = Image.open(btndua1)
    btndua3 = btndua2.resize((120, 25))
    btndua4 = ImageTk.PhotoImage(btndua3)
    btndua5 = tk.Button(dokter, image=btndua4, background="white", relief=FLAT, command=duakali)
    btndua5.place(x=1057, y=808)

    # ====
    def tigakali():
        txttiga = " 3x Sehari " 
        resepentry.insert(tk.END, txttiga)
    btntiga1 = "button tiga kali.png"
    btntiga2 = Image.open(btntiga1)
    btntiga3 = btntiga2.resize((120, 25))
    btntiga4 = ImageTk.PhotoImage(btntiga3)
    btntiga5 = tk.Button(dokter, image=btntiga4, background="white", relief=FLAT, command=tigakali)
    btntiga5.place(x=1190, y=808)

    # ====
    def sebelum():
        txtsebelum = " Sebelum Makan "  
        resepentry.insert(tk.END, txtsebelum)
    btnsblm1 = "button sebelum.png"
    btnsblm2 = Image.open(btnsblm1)
    btnsblm3 = btnsblm2.resize((190, 30))
    btnsblm4 = ImageTk.PhotoImage(btnsblm3)
    btnsblm5 = tk.Button(dokter, image=btnsblm4, background="white", relief=FLAT, command=sebelum)
    btnsblm5.place(x=921, y=840)

    # ====
    def sesudah():
        txtsesudah = " Sesudah Makan "  
        resepentry.insert(tk.END, txtsesudah)
    btnssdh1 = "button sesudah.png"
    btnssdh2 = Image.open(btnssdh1)
    btnssdh3 = btnssdh2.resize((190, 30))
    btnssdh4 = ImageTk.PhotoImage(btnssdh3)
    btnssdh5 = tk.Button(dokter, image=btnssdh4, background="white", relief=FLAT, command=sesudah)
    btnssdh5.place(x=1120, y=840)

    # ====
    def dokter_dashboard(): 
        dokter.withdraw()
        dashboard.deiconify()
    btndashdk1 = "button beranda side.png"
    btndashdk2 = Image.open(btndashdk1)
    btndashdk3 = btndashdk2.resize((100, 18))
    btndashdk4 = ImageTk.PhotoImage(btndashdk3)
    btndashdk5 = tk.Button(dokter, image=btndashdk4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dokter_dashboard)
    btndashdk5.place(x=100, y=189)

    # ====
    def dokter_bpjs(): 
        dokter.withdraw()
        databpjs_page()
    btnbpjsdk1 = "button data bpjs side.png"
    btnbpjsdk2 = Image.open(btnbpjsdk1)
    btnbpjsdk3 = btnbpjsdk2.resize((100, 18))
    btnbpjsdk4 = ImageTk.PhotoImage(btnbpjsdk3)
    btnbpjsdk5 = tk.Button(dokter, image=btnbpjsdk4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dokter_bpjs)
    btnbpjsdk5.place(x=100, y=263)

    # ====
    def dokter_pelayanan(): 
        dokter.withdraw()
        pelayanan.deiconify()
    fedcbbtnsdc1 = "button pelayanan side.png"
    fedcbbtnsdc2 = Image.open(fedcbbtnsdc1)
    fedcbbtnsdc3 = fedcbbtnsdc2.resize((110, 25))
    fedcbbtnsdc4 = ImageTk.PhotoImage(fedcbbtnsdc3)
    fedcbbtnsdc5 = tk.Button(dokter, image=fedcbbtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dokter_pelayanan)
    fedcbbtnsdc5.place(x=100, y=338)

    # ====
    def dokter_antrian(): 
        dokter.withdraw()
        antrian.deiconify()
    fedcbbtnsdd1 = "button antrian side.png"
    fedcbbtnsdd2 = Image.open(fedcbbtnsdd1)
    fedcbbtnsdd3 = fedcbbtnsdd2.resize((95, 18))
    fedcbbtnsdd4 = ImageTk.PhotoImage(fedcbbtnsdd3)
    fedcbbtnsdd5 = tk.Button(dokter, image=fedcbbtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dokter_antrian)
    fedcbbtnsdd5.place(x=100, y=419)


    # ====
    btndkrsd1 = "button dokter side.png"
    btndkrsd2 = Image.open(btndkrsd1)
    btndkrsd3 = btndkrsd2.resize((95, 18))
    btndkrsd4 = ImageTk.PhotoImage(btndkrsd3)
    btndkrsd5 = tk.Button(dokter, image=btndkrsd4, borderwidth=0, highlightthickness=0, relief=FLAT)
    btndkrsd5.place(x=100, y=497)


    # ====
    def update_apoteker_label():
        tgientry_value = tgientry.get("1.0", "end-1c")
        brtentry_value = brtentry.get("1.0", "end-1c")
        lbltgientry.config(text=tgientry_value)
        lblbrtentry.config(text=brtentry_value)

    def dokter_apoteker():
        update_apoteker_label()  
        dokter.withdraw()  
        apoteker.deiconify()

    btnaposd1 = "button apoteker side.png"
    btnaposd2 = Image.open(btnaposd1)
    btnaposd3 = btnaposd2.resize((100, 25))
    btnaposd4 = ImageTk.PhotoImage(btnaposd3)
    btnaposd5 = tk.Button(dokter, image=btnaposd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dokter_apoteker)
    btnaposd5.place(x=100, y=572)

    # ====
    def dokter_login(): 
        dokter.withdraw()
        login.deiconify()
    fedcbbtnsdg1 = "button keluar side.png"
    fedcbbtnsdg2 = Image.open(fedcbbtnsdg1)
    fedcbbtnsdg3 = fedcbbtnsdg2.resize((90, 18))
    fedcbbtnsdg4 = ImageTk.PhotoImage(fedcbbtnsdg3)
    fedcbbtnsdg5 = tk.Button(dokter, image=fedcbbtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dokter_login)
    fedcbbtnsdg5.place(x=100, y=652)

    # ====
    label_time = tk.Label(dokter, border=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    label_date = tk.Label(dokter, border=0, font=('Century Gothic Bold', 17))
    label_date.place(x=150, y=862, anchor="center")
    label_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        dokter.after(1000, update_time_date)  
    update_time_date()
    
# ===============================================HALAMAN APOTEKER===========================================

    apoteker = tk.Toplevel()
    apoteker.title("Apoteker")
    width, height = apoteker.winfo_screenwidth(), apoteker.winfo_screenheight()
    apoteker.geometry(f"{width}x{height}")
    apoteker.configure(bg="#C8E8F5")
    apoteker.resizable(False, False)

    bgapoteker1 = "bg apoteker.png"
    bgapoteker2 = Image.open(bgapoteker1)
    bgapoteker3 = bgapoteker2.resize((1550, 930))
    bgapoteker4 = ImageTk.PhotoImage(bgapoteker3)
    bgapoteker5 = tk.Label(apoteker, image=bgapoteker4, bd=0)
    bgapoteker5.place(x=0, y=0)

    lblresep = tk.Label(apoteker, text="", background="white",font=20, anchor="w", justify="left")
    lblresep.pack(pady=10)
    lblresep.place(x=375, y=390)

    lbltgientry = tk.Label(apoteker, text="", background="#ffffff", font=('Bahnschrift',14))
    lbltgientry.place(x=1135, y=472)

    lblbrtentry = tk.Label(apoteker, text="", background="#ffffff", font=('Bahnschrift',14))
    lblbrtentry.place(x=1135, y=503)

    def translate_month(month):
        months = {
        'January': 'Januari', 'February': 'Februari', 'March': 'Maret', 'April': 'April', 
        'May': 'Mei', 'June': 'Juni', 'July': 'Juli', 'August': 'Agustus', 
        'September': 'September', 'October': 'Oktober', 'November': 'November', 'December': 'Desember'}
        return months[month]

    def get_current_date_in_indonesian():
        now = datetime.now()
        day = now.strftime("%d")
        month = now.strftime("%B")
        year = now.strftime("%Y")
        month_indonesian = translate_month(month)
        return f"{day} {month_indonesian} {year}"
    
    with open('datastaf.json', 'r') as file:
        datadokter = json.load(file)
    def cari_staf_berdasarkan_id(id_staf):
        for nama, info in datadokter.items():
            if info['ID'] == id_staf:
                return nama, info['ID']
        return None, None

    def print_to_pdf():
        pdf = FPDF()
        pdf.add_page()

        image_path = "resep.jpeg"  
        pdf.image(image_path, x=0, y=0, w=210, h=297)
        pdf.set_font("Arial", size=12)

        text = lblresep.cget("text")
        lines = text.split('\n')
        start_x = 20  
        start_y = 197  
        pdf.set_y(start_y)
        for line in lines:
            pdf.set_x(start_x)  
            pdf.cell(0, 6, line, ln=True)

        keluh = keluhanentry.get("1.0", "end-1c")
        baris = keluh.split('\n')
        pdf.set_y(97)
        for line in baris:
            pdf.set_x(20)  
            pdf.cell(0, 6, line, ln=True)

        getid = iddokterentry.get("1.0", "end-1c")
        nama_dokter, id_dokter = cari_staf_berdasarkan_id(getid)

        namadokter=nama_dokter
        iddokter=id_dokter
        brt = brtentry.get("1.0", "end-1c")    
        tgi = tgientry.get("1.0", "end-1c")
        nmpasienpdf= nmpasienout.cget("text")
        umrpasienpdf= umrpasienout.cget("text")

        additional_text = [("Nama Dokter :", namadokter, 10, 30),
                       ("Nomor ID       :", iddokter, 10, 36),
                       ("Nama Pasien :", nmpasienpdf, 10, 48),
                       ("Umur              :", umrpasienpdf, 10, 54),
                       ("Berat Badan   :", brt, 10, 60),
                       ("Tinggi Badan  :", tgi, 10, 66)]
        for label, value, x, y in additional_text:
            pdf.set_xy(x, y)
            pdf.cell(0, 10, f"{label} {value}", ln=True)

        tanggal = get_current_date_in_indonesian()
        pdf.set_xy(158, 30)
        pdf.cell(0, 10, f"Surabaya, {tanggal}", ln=True)
    
        time = datetime.now().strftime("%H.%M") 
        file_name = f"{nmpasienpdf} {time}.pdf"   

        timefile = datetime.now().strftime("%d-%m-%Y")
        folder_name = fr'C:\Users\nachla\OneDrive\文档\STRUKTUR DATA dan ALGORITMA\PROJEK\GASSSSSSIN\GASSSSSSIN\History Resep\{timefile}'


        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        fullpath = os.path.join(folder_name, file_name)
        pdf.output(fullpath)
        messagebox.showinfo("Berhasil", f"Resep telah dibuat dengan nama '{fullpath}'")
        hapusentrydokter()

    btnctk1 = "button cetak.png"
    btnctk2 = Image.open(btnctk1)
    btnctk3 = btnctk2.resize((465, 42))
    btnctk4 = ImageTk.PhotoImage(btnctk3)
    btnctk5 = tk.Button(apoteker, image=btnctk4, borderwidth=0,highlightthickness=0, relief=FLAT, command=print_to_pdf)
    btnctk5.place(x=400, y=800)

    # =====
    def apoteker_dashboard():
        apoteker.withdraw()  
        dashboard.deiconify()
    gbtndashdk1 = "button beranda side.png"
    gbtndashdk2 = Image.open(gbtndashdk1)
    gbtndashdk3 = gbtndashdk2.resize((100, 18))
    gbtndashdk4 = ImageTk.PhotoImage(gbtndashdk3)
    gbtndashdk5 = tk.Button(apoteker, image=gbtndashdk4, borderwidth=0, highlightthickness=0, relief=FLAT, command=apoteker_dashboard)
    gbtndashdk5.place(x=100, y=189)

    # =====
    def apoteker_bpjs():
        apoteker.withdraw()  
        databpjs_page()
    gbtnbpjsdk1 = "button data bpjs side.png"
    gbtnbpjsdk2 = Image.open(gbtnbpjsdk1)
    gbtnbpjsdk3 = gbtnbpjsdk2.resize((100, 18))
    gbtnbpjsdk4 = ImageTk.PhotoImage(gbtnbpjsdk3)
    gbtnbpjsdk5 = tk.Button(apoteker, image=gbtnbpjsdk4, borderwidth=0, highlightthickness=0, relief=FLAT, command=apoteker_bpjs)
    gbtnbpjsdk5.place(x=100, y=263)

    # =====
    def apoteker_pelayanan():
        apoteker.withdraw()  
        pelayanan.deiconify()
    gfedcbbtnsdc1 = "button pelayanan side.png"
    gfedcbbtnsdc2 = Image.open(gfedcbbtnsdc1)
    gfedcbbtnsdc3 = gfedcbbtnsdc2.resize((110, 25))
    gfedcbbtnsdc4 = ImageTk.PhotoImage(gfedcbbtnsdc3)
    gfedcbbtnsdc5 = tk.Button(apoteker, image=gfedcbbtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=apoteker_pelayanan)
    gfedcbbtnsdc5.place(x=100, y=338)

    # =====
    def apoteker_antrian():
        apoteker.withdraw()  
        antrian.deiconify()
    gfedcbbtnsdd1 = "button antrian side.png"
    gfedcbbtnsdd2 = Image.open(gfedcbbtnsdd1)
    gfedcbbtnsdd3 = gfedcbbtnsdd2.resize((95, 18))
    gfedcbbtnsdd4 = ImageTk.PhotoImage(gfedcbbtnsdd3)
    gfedcbbtnsdd5 = tk.Button(apoteker, image=gfedcbbtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=apoteker_antrian)
    gfedcbbtnsdd5.place(x=100, y=419)


    # =====
    def apoteker_dokter():
        apoteker.withdraw()  
        dokter.deiconify()
    bttndkrsd1 = "button dokter side.png"
    bttndkrsd2 = Image.open(bttndkrsd1)
    bttndkrsd3 = bttndkrsd2.resize((95, 18))
    bttndkrsd4 = ImageTk.PhotoImage(bttndkrsd3)
    bttndkrsd5 = tk.Button(apoteker, image=bttndkrsd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=apoteker_dokter)
    bttndkrsd5.place(x=100, y=497)


    # =====
    bttnaposd1 = "button apoteker side.png"
    bttnaposd2 = Image.open(bttnaposd1)
    bttnaposd3 = bttnaposd2.resize((100, 25))
    bttnaposd4 = ImageTk.PhotoImage(bttnaposd3)
    bttnaposd5 = tk.Button(apoteker, image=bttnaposd4, borderwidth=0,highlightthickness=0, relief=FLAT)
    bttnaposd5.place(x=100, y=572)

    # =====
    def apoteker_login():
        apoteker.withdraw()  
        login.deiconify()
    gfedcbbtnsdg1 = "button keluar side.png"
    gfedcbbtnsdg2 = Image.open(gfedcbbtnsdg1)
    gfedcbbtnsdg3 = gfedcbbtnsdg2.resize((90, 18))
    gfedcbbtnsdg4 = ImageTk.PhotoImage(gfedcbbtnsdg3)
    gfedcbbtnsdg5 = tk.Button(apoteker, image=gfedcbbtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=apoteker_login)
    gfedcbbtnsdg5.place(x=100, y=652)

    # =====
    label_time = tk.Label(apoteker, border=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    label_date = tk.Label(apoteker, border=0, font=('Century Gothic Bold', 17))
    label_date.place(x=150, y=862, anchor="center")
    label_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        apoteker.after(1000, update_time_date)  
    update_time_date()

    pelayanan.mainloop()

# ===============================================HALAMAN TENTANG=======================================
def tentang_page(parent):
    global dashboard, tentang
    tentang=tk.Toplevel(parent)
    tentang.title("Tentang Sistem")
    width, height = tentang.winfo_screenwidth(), tentang.winfo_screenheight()
    tentang.geometry(f"{width}x{height}")
    tentang.configure(bg="#C8E8F5")
    tentang.resizable(False, False)

    bgtentang1 = "bg tentang.png"
    bgtentang2 = Image.open(bgtentang1)
    bgtentang3 = bgtentang2.resize((1550, 930))
    bgtentang4 = ImageTk.PhotoImage(bgtentang3)
    bgtentang5 = tk.Label(tentang, image=bgtentang4, bd=0)
    bgtentang5.place(x=0, y=0)

    hallostaf = Label(tentang, text=f"Hallo, {Namastaf}", font=('Century Gothic bold italic', 17), fg='#024480', bg='#FAFAFA')
    width_text = hallostaf.winfo_reqwidth()
    x_coordinate = width - width_text - 40
    hallostaf.place(x=x_coordinate, y=40)

    # =====
    def tentang_dashboard():
        tentang.destroy()
        dashboard.deiconify() 

    abtnsda1 = "button beranda side.png"
    abtnsda2 = Image.open(abtnsda1)
    abtnsda3 = abtnsda2.resize((100, 18))
    abtnsda4 = ImageTk.PhotoImage(abtnsda3)
    abtnsda5 = tk.Button(tentang, image=abtnsda4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_dashboard)
    abtnsda5.place(x=100, y=189)
    # =====
    def tentang_bpjs():
        tentang.withdraw()
        databpjs_page()

    abtnsdb1 = "button data bpjs side.png"
    abtnsdb2 = Image.open(abtnsdb1)
    abtnsdb3 = abtnsdb2.resize((100, 18))
    abtnsdb4 = ImageTk.PhotoImage(abtnsdb3)
    abtnsdb5 = tk.Button(tentang, image=abtnsdb4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_bpjs)
    abtnsdb5.place(x=100, y=263)

    # =====
    def tentang_pelayanan():
        tentang.withdraw()
        pelayanan.deiconify()

    abtnsdc1 = "button pelayanan side.png"
    abtnsdc2 = Image.open(abtnsdc1)
    abtnsdc3 = abtnsdc2.resize((110, 25))
    abtnsdc4 = ImageTk.PhotoImage(abtnsdc3)
    abtnsdc5 = tk.Button(tentang, image=abtnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_pelayanan)
    abtnsdc5.place(x=100, y=338)

    # =====
    def tentang_antrian():
        tentang.withdraw()
        antrian.deiconify()

    abtnsdd1 = "button antrian side.png"
    abtnsdd2 = Image.open(abtnsdd1)
    abtnsdd3 = abtnsdd2.resize((95, 18))
    abtnsdd4 = ImageTk.PhotoImage(abtnsdd3)
    abtnsdd5 = tk.Button(tentang, image=abtnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_antrian)
    abtnsdd5.place(x=100, y=419)


    # =====
    def tentang_dokter():  
        tentang.withdraw()
        dokter.deiconify()

    abtnsde1 = "button dokter side.png"
    abtnsde2 = Image.open(abtnsde1)
    abtnsde3 = abtnsde2.resize((95, 18))
    abtnsde4 = ImageTk.PhotoImage(abtnsde3)
    abtnsde5 = tk.Button(tentang, image=abtnsde4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_dokter)
    abtnsde5.place(x=100, y=497)


    # =====
    def tentang_apoteker():  
        tentang.withdraw()
        apoteker.deiconify()

    abtnsdf1 = "button apoteker side.png"
    abtnsdf2 = Image.open(abtnsdf1)
    abtnsdf3 = abtnsdf2.resize((100, 25))
    abtnsdf4 = ImageTk.PhotoImage(abtnsdf3)
    abtnsdf5 = tk.Button(tentang, image=abtnsdf4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_apoteker)
    abtnsdf5.place(x=100, y=572)
    # =====
    def tentang_login(): 
        tentang.withdraw() 
        login.deiconify()
        
    abtnsdg1 = "button keluar side.png"
    abtnsdg2 = Image.open(abtnsdg1)
    abtnsdg3 = abtnsdg2.resize((90, 18))
    abtnsdg4 = ImageTk.PhotoImage(abtnsdg3)
    abtnsdg5 = tk.Button(tentang, image=abtnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=tentang_login)
    abtnsdg5.place(x=100, y=652)

    # =====
    ablabel_time = tk.Label(tentang, border=0, font=('Century Gothic Bold', 30))
    ablabel_time.place(x=150, y=815, anchor="center")
    ablabel_time.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    ablabel_date = tk.Label(tentang, border=0, font=('Century Gothic Bold', 17))
    ablabel_date.place(x=150, y=862, anchor="center")
    ablabel_date.config(bg="#668DAE",fg="#FFFFFF", highlightthickness=0)
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        ablabel_time.config(text=current_time)
        ablabel_date.config(text=current_date)
        tentang.after(1000, update_time_date) 
    update_time_date()


    tentang.mainloop()

# ===============================================HALAMAN DASHBOARD=====================================
def dashboard_page():
    global dashboard, jumlah_bpjs
    dashboard = tk.Toplevel(login)
    dashboard.title("Main Page")
    width, height = dashboard.winfo_screenwidth(), dashboard.winfo_screenheight()
    dashboard.geometry(f"{width}x{height}")
    dashboard.resizable(False,False)

    bgdashboard1 = "bg dashboard.png"
    bgdashboard2 = Image.open(bgdashboard1)
    bgdashboard3 = bgdashboard2.resize((1550, 930))
    bgdashboard4 = ImageTk.PhotoImage(bgdashboard3)
    bgdashboard5 = tk.Label(dashboard, image=bgdashboard4, bd=0)
    bgdashboard5.place(x=0, y=0)

    # =====
    def hitung_staf():
        with open('datastaf.json', 'r') as f:
            data_staf = json.load(f)
        jumlah_staf = len(data_staf)
        return jumlah_staf
    jumlah_staf = hitung_staf()
    jumlahstaf = tk.Label(dashboard, text=f"{jumlah_staf} Orang", font=('Century Gothic bold', 22), fg='#1D987C', bg='#FFFFFF' )
    jumlahstaf.place(x=780, y=445)

    def hitung_pasien_bpjs():
        with open('databpjs.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            jumlah_bpjs = sum(1 for row in reader)
        return jumlah_bpjs
    jumlah_bpjs = hitung_pasien_bpjs()
    jumlahpasien = Label(dashboard, text=f"{jumlah_bpjs} Orang", font=('Century Gothic bold', 22), fg='#1D987C', bg='#FFFFFF')
    jumlahpasien.place(x=780, y=535)
    hitung_pasien_bpjs()

    # =====
    profilestaf = Label(dashboard, text=f"{Namastaf}", font=('Century Gothic bold', 26), fg="#024480", bg="white")
    profilestaf.place(x=450, y=290)

    profilejabatan = Label(dashboard, text=f"{jabatan}", font=('Century Gothic bold italic', 17), fg="#1D987C", bg="white")
    profilejabatan.place(x=450, y=335)

    hallostaf = Label(dashboard, text=f"Hallo, {Namastaf}", font=('Century Gothic bold italic', 17), fg='#024480', bg='#FAFAFA')
    width_text = hallostaf.winfo_reqwidth()
    x_coordinate = width - width_text - 40
    hallostaf.place(x=x_coordinate, y=40)
    
    # =====
    cal_frame = tk.Frame(dashboard, bg="#C8E8F5")
    cal_frame.place(x=1038, y=340, width=450, height=230)
    cal = Calendar(
        cal_frame,
        selectmode="day",
        date_pattern="Y-mm-dd",
        background="#4E7CA0",       
        foreground="white",    
        bordercolor="#B2E1F7",
        headersbackground="#B2E1F7",       
        selectbackground="#4E7CA0",      
        selectforeground="white",     
        weekendbackground="white",
        weekendforeground="black",      
        othermonthbackground="#E8ECED",  
        othermonthforeground="#E8ECED",
        othermonthwebackground="#E8ECED",
        othermonthweforeground="#E8ECED",
        showweeknumbers=False)
    cal.pack(fill="both", expand=True)

    # =====
    def update_time_date():
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d %B %Y")
        label_time.config(text=current_time)
        label_date.config(text=current_date)
        dashboard.after(1000, update_time_date) 

    label_time = tk.Label(dashboard, border=0, bg="#668DAE",fg="#FFFFFF", highlightthickness=0, font=('Century Gothic Bold', 30))
    label_time.place(x=150, y=815, anchor="center")
    label_date = tk.Label(dashboard, border=0, bg="#668DAE",fg="#FFFFFF", highlightthickness=0 ,font=('Century Gothic Bold', 17))
    label_date.place(x=145, y=862, anchor="center")
    update_time_date()

    # =====
    def dashboard_tentang():
        dashboard.withdraw()
        tentang_page(dashboard)

    btnabout1 = "button tentang.png"
    btnabout2 = Image.open(btnabout1)
    btnabout3 = btnabout2.resize((330, 40))
    btnabout4 = ImageTk.PhotoImage(btnabout3)
    btnabout5 = tk.Button(dashboard, image=btnabout4, background="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_tentang)
    btnabout5.place(x=1035, y=187)

    btnsda1 = "button beranda side.png"
    btnsda2 = Image.open(btnsda1)
    btnsda3 = btnsda2.resize((100, 18))
    btnsda4 = ImageTk.PhotoImage(btnsda3)
    btnsda5 = tk.Button(dashboard, image=btnsda4, borderwidth=0, highlightthickness=0, relief=FLAT)
    btnsda5.place(x=100, y=189)

    # =====
    def dashboard_bpjs():
        dashboard.withdraw()
        databpjs_page()

    btnsdb1 = "button data bpjs side.png"
    btnsdb2 = Image.open(btnsdb1)
    btnsdb3 = btnsdb2.resize((100, 18))
    btnsdb4 = ImageTk.PhotoImage(btnsdb3)
    btnsdb5 = tk.Button(dashboard, image=btnsdb4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_bpjs)
    btnsdb5.place(x=100, y=263)

    btnbwha1 = "button data bpjs.png" 
    btnbwha2 = Image.open(btnbwha1)
    btnbwha3 = btnbwha2.resize((200, 200))
    btnbwha4 = ImageTk.PhotoImage(btnbwha3)
    btnbwha5 = tk.Button(dashboard, image=btnbwha4, background="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_bpjs)
    btnbwha5.place(x=350, y=660)
    # =====
    def dashboard_pelayanan():
        dashboard.withdraw()
        pelayanan.deiconify()
    
    btnsdc1 = "button pelayanan side.png"
    btnsdc2 = Image.open(btnsdc1)
    btnsdc3 = btnsdc2.resize((110, 25))
    btnsdc4 = ImageTk.PhotoImage(btnsdc3)
    btnsdc5 = tk.Button(dashboard, image=btnsdc4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_pelayanan)
    btnsdc5.place(x=100, y=338)

    btnbwhb1 = "button pelayanan.png"
    btnbwhb2 = Image.open(btnbwhb1)
    btnbwhb3 = btnbwhb2.resize((200, 200))
    btnbwhb4 = ImageTk.PhotoImage(btnbwhb3)
    btnbwhb5 = tk.Button(dashboard, image=btnbwhb4, background="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_pelayanan)
    btnbwhb5.place(x=585, y=660)

    # =====
    def dashboard_antrian():
        dashboard.withdraw()
        antrian.deiconify()
    
    btnsdd1 = "button antrian side.png"
    btnsdd2 = Image.open(btnsdd1)
    btnsdd3 = btnsdd2.resize((95, 18))
    btnsdd4 = ImageTk.PhotoImage(btnsdd3)
    btnsdd5 = tk.Button(dashboard, image=btnsdd4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_antrian)
    btnsdd5.place(x=100, y=419)

    btnbwhc1 = "button antrian.png"
    btnbwhc2 = Image.open(btnbwhc1)
    btnbwhc3 = btnbwhc2.resize((200, 200))
    btnbwhc4 = ImageTk.PhotoImage(btnbwhc3)
    btnbwhc5 = tk.Button(dashboard, image=btnbwhc4, background="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_antrian)
    btnbwhc5.place(x=820, y=662)

    # =====
    def dashboard_dokter():
        dashboard.withdraw()
        dokter.deiconify()

    btnsde1 = "button dokter side.png"
    btnsde2 = Image.open(btnsde1)
    btnsde3 = btnsde2.resize((95, 18))
    btnsde4 = ImageTk.PhotoImage(btnsde3)
    btnsde5 = tk.Button(dashboard, image=btnsde4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_dokter)
    btnsde5.place(x=100, y=497)

    btnbwhd1 = "button dokter.png"
    btnbwhd2 = Image.open(btnbwhd1)
    btnbwhd3 = btnbwhd2.resize((200, 200))
    btnbwhd4 = ImageTk.PhotoImage(btnbwhd3)
    btnbwhd5 = tk.Button(dashboard, image=btnbwhd4, background="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_dokter)
    btnbwhd5.place(x=1060, y=660)

    # =====
    def dashboard_apoteker():
        dashboard.withdraw()
        apoteker.deiconify()

    btnsdf1 = "button apoteker side.png"
    btnsdf2 = Image.open(btnsdf1)
    btnsdf3 = btnsdf2.resize((100, 25))
    btnsdf4 = ImageTk.PhotoImage(btnsdf3)
    btnsdf5 = tk.Button(dashboard, image=btnsdf4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_apoteker)
    btnsdf5.place(x=100, y=572)

    btnbwhe1 = "button apoteker.png"
    btnbwhe2 = Image.open(btnbwhe1)
    btnbwhe3 = btnbwhe2.resize((200, 200))
    btnbwhe4 = ImageTk.PhotoImage(btnbwhe3)
    btnbwhe5 = tk.Button(dashboard, image=btnbwhe4, background="white", borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_apoteker)
    btnbwhe5.place(x=1295, y=662)

    # =====
    def dashboard_login():
        dashboard.withdraw()
        login.deiconify()

    btnsdg1 = "button keluar side.png"
    btnsdg2 = Image.open(btnsdg1)
    btnsdg3 = btnsdg2.resize((90, 18))
    btnsdg4 = ImageTk.PhotoImage(btnsdg3)
    btnsdg5 = tk.Button(dashboard, image=btnsdg4, borderwidth=0, highlightthickness=0, relief=FLAT, command=dashboard_login)
    btnsdg5.place(x=100, y=652)

    dashboard.mainloop()

# ===============================================HALAMAN REGISTRASI========================================
def daftarstaf_page(parent):
    daftarstaf = tk.Toplevel(parent)
    daftarstaf.title("Daftar staf")
    width, height = daftarstaf.winfo_screenwidth(), daftarstaf.winfo_screenheight()
    daftarstaf.geometry(f"{width}x{height}")
    daftarstaf.resizable(False,False)

    bgdaftarstaf1 = "bg daftar staf.png"
    bgdaftarstaf2 = Image.open(bgdaftarstaf1)
    bgdaftarstaf3 = bgdaftarstaf2.resize((1525, 945))
    bgdaftarstaf4 = ImageTk.PhotoImage(bgdaftarstaf3)
    bgdaftarstaf5 = tk.Label(daftarstaf, image=bgdaftarstaf4, bd=0)   
    bgdaftarstaf5.place(x=0, y=0,)

    def on_enter_nama(e):
        namastaf_dftr.delete(0,'end')
    def on_leave_nama(e):
        name=namastaf_dftr.get()
        if name =='':
            namastaf_dftr.insert(0,'')
    namastaf_dftr = Entry(daftarstaf, width=28, fg='#1F4C73', border =0, bg='#FAFAFA', font=('Bahnschrift',17))
    namastaf_dftr.place(x=960, y=443)
    namastaf_dftr.insert(0,"")
    namastaf_dftr.bind('<FocusIn>', on_enter_nama)
    namastaf_dftr.bind('<FocusOut>', on_leave_nama)
    # Frame(daftarstaf,width=250,height=3,bg='white').place(x=55,y=107)

    def on_enter_id(e):
        idstaf_dftr.delete(0,'end')
    def on_leave_id(e):
        kata=idstaf_dftr.get()
        if kata =='*':
            idstaf_dftr.insert(0,'')
    idstaf_dftr = Entry(daftarstaf, width=28, fg='#1F4C73', border =0, bg='#FAFAFA', font=('Bahnschrift',17))
    idstaf_dftr.place(x=960, y=554)
    idstaf_dftr.insert(0,'')
    idstaf_dftr.bind('<FocusIn>', on_enter_id)
    idstaf_dftr.bind('<FocusOut>', on_leave_id)

    jabatan_options = ["Dokter", "Apoteker", "Pelayanan"]
    jabatan_combo = ttk.Combobox(daftarstaf, values=jabatan_options, state="readonly", font=('Bahnschrift', 17), width=30)
    jabatan_combo.place(x=960, y=668)

    def registrasi():
        Namastaf = namastaf_dftr.get()
        IDstaf = idstaf_dftr.get()
        Jabatan = jabatan_combo.get()
        
        if not Namastaf or not IDstaf or not Jabatan:
            messagebox.showerror("Perhatian", "Entry tidak boleh kosong")
            return
        elif Namastaf and IDstaf and Jabatan:
            datastaf[Namastaf] = {'ID': IDstaf, 'Jabatan': Jabatan}
            with open('datastaf.json', 'w') as file:
                json.dump(datastaf, file)
            messagebox.showinfo('Signup', 'Registrasi berhasil')
        daftarstaf.destroy()

    btndftrr1 = "button daftar.png"
    btndftrr2 = Image.open(btndftrr1)
    btndftrr3 = btndftrr2.resize((300, 45))
    btndftrr4 = ImageTk.PhotoImage(btndftrr3)
    btndftrr5 = tk.Button(daftarstaf, image=btndftrr4, borderwidth=0, highlightthickness=0, relief=FLAT, command=registrasi)
    btndftrr5.place(x=1050, y=740)

    def daftarstaf_login():          
        daftarstaf.destroy()

    btnbcklgn1 = "button back.png"
    btnbcklgn2 = Image.open(btnbcklgn1)
    btnbcklgn3 = btnbcklgn2.resize((90, 45))
    btnbcklgn4 = ImageTk.PhotoImage(btnbcklgn3)
    btnbcklgn5 = tk.Button(daftarstaf, image=btnbcklgn4, borderwidth=0, highlightthickness=0, relief=FLAT, command=daftarstaf_login)
    btnbcklgn5.place(x=940, y=740)

    daftarstaf.mainloop()
# ===============================================HALAMAN LOGIN==================================================

login = tk.Tk()
login.title("Login")
width, height = login.winfo_screenwidth(), login.winfo_screenheight()
login.geometry(f"{width}x{height}")
login.resizable(False,False)

try:
    with open("datastaf.json", 'r') as file:
        datastaf = json.load(file)
except FileNotFoundError:
    datastaf = {}

bglogin1 = "bg login.png"
bglogin2 = Image.open(bglogin1)
bglogin3 = bglogin2.resize((1525, 945))
bglogin4 = ImageTk.PhotoImage(bglogin3)
bglogin5 = tk.Label(login, image=bglogin4, bd=0)
bglogin5.place(x=0, y=0)

def on_enternm(e):
    namastaflogin.delete(0,'end')
def on_leavenm(e):
    name=namastaflogin.get()
    if name =='':
        namastaflogin.insert(0,'')

namastaflogin = Entry(login, width=25, fg='#1F4C73', border =0, bg='#FAFAFA', font=('Bahnschrift',20))
namastaflogin.place(x=960, y=460)
namastaflogin.insert(0,'')
namastaflogin.bind('<FocusIn>', on_enternm)
namastaflogin.bind('<FocusOut>', on_leavenm)

def on_enterid(e):
    idstaflogin.delete(0,'end')
def on_leaveid(e):
    name=idstaflogin.get()
    if name =='':
        idstaflogin.insert(0,'')

idstaflogin = Entry(login, width=25, fg='#1F4C73', border =0, bg='#FAFAFA', font=('Bahnschrift',20))
idstaflogin.place(x= 960, y=570)
idstaflogin.insert(0,'')
idstaflogin.bind('<FocusIn>', on_enterid)
idstaflogin.bind('<FocusOut>', on_leaveid)

def hapus_entry_login():
    namastaflogin.delete(0, tk.END)
    idstaflogin.delete(0, tk.END)

def masuk():
    global Namastaf, jabatan
    Namastaf = namastaflogin.get()
    IDstaf = idstaflogin.get()
    if Namastaf in datastaf and IDstaf == datastaf[Namastaf]['ID']:
        jabatan = datastaf[Namastaf]['Jabatan']
        login.withdraw()
        hapus_entry_login()
        dashboard_page()
    else:
        messagebox.showerror("Invalid", "Nama pengguna atau Kata kunci salah")
    

btnlogin1 = "button login.png"
btnlogin2 = Image.open(btnlogin1)
btnlogin3 = btnlogin2.resize((300, 45))
btnlogin4 = ImageTk.PhotoImage(btnlogin3)
btnlogin5 = tk.Button(login, image=btnlogin4, borderwidth=0, highlightthickness=0, relief=FLAT, command=masuk)
btnlogin5.place(x=1030, y=645)

def login_daftar():
    daftarstaf_page(login)

btndftr1 = "button tambah staf.png"
btndftr2 = Image.open(btndftr1)
btndftr3 = btndftr2.resize((300, 45))
btndftr4 = ImageTk.PhotoImage(btndftr3)
btndftr5 = tk.Button(login, image=btndftr4, borderwidth=0, highlightthickness=0, relief=FLAT, command=login_daftar)
btndftr5.place(x=1030, y=710)

system_page()
login.mainloop()