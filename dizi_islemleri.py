import tkinter as tk
from tkinter import messagebox, simpledialog

def en_kucuk(dizi):
    enk = dizi[0]
    for eleman in dizi:
        if eleman < enk:
            enk = eleman
    return enk

def en_buyuk(dizi):
    enb = dizi[0]
    for eleman in dizi:
        if eleman > enb:
            enb = eleman
    return enb

def toplam(dizi):
    toplam_deger = 0
    for eleman in dizi:
        toplam_deger += eleman
    return toplam_deger

def ortalama(dizi):
    return toplam(dizi) / len(dizi)

def std_sapma(dizi):
    ort = ortalama(dizi)
    farklarin_karesi_toplami = 0
    for eleman in dizi:
        farklarin_karesi_toplami += (eleman - ort) ** 2
        
    varyans = farklarin_karesi_toplami  / len(dizi)
    return varyans ** 0.5

def islemleri_baslat():
    m = simpledialog.askinteger("Dizi Elemanları", "Eleman sayısını giriniz : ", parent=pencere)
    if not m or m<=0:
        return
    
    dizi = []
    
    for i in range(m):
        pencere.update()
        deger = simpledialog.askfloat("Dizi Elemanları", f"{i+1}. elemanı giriniz:",parent=pencere)
        
        if deger is None:
            messagebox.showwarning("Uyarı","İptal edildi")
            return
        dizi.append(deger)
        
    sonuc_metni = (
        f"Eleman sayısı: {len(dizi)}\n"
        f"En büyük eleman: {en_buyuk(dizi)}\n"
        f"En küçük eleman: {en_kucuk(dizi)}\n"
        f"Toplam: {toplam(dizi)}\n"
        f"Ortalama: {ortalama(dizi):.2f}\n"
        f"Standart sapma: {std_sapma(dizi):.2f}"
    )
    
    text_sonuc.config(state=tk.NORMAL)
    text_sonuc.delete(1.0, tk.END)
    text_sonuc.insert(tk.END, sonuc_metni)
    text_sonuc.config(state=tk.DISABLED)

pencere = tk.Tk()
pencere.title("Dizi İslemleri")
pencere.geometry("350x200")

btn_baslat = tk.Button(pencere, text="Dizi Verileri Gir", command= islemleri_baslat, width=15)
btn_baslat.pack(side=tk.TOP, pady=15)

text_sonuc = tk.Text(pencere, height=8,width=30,bg=pencere.cget("background"), bd=0, font=("Arial",10))
text_sonuc.pack(side=tk.TOP,pady=5,padx=10)
text_sonuc.config(state=tk.DISABLED)

pencere.mainloop()
