from pathlib import Path
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Frame, Label, scrolledtext, LabelFrame, IntVar, messagebox, filedialog, StringVar
from tkinter import ttk, scrolledtext, messagebox, filedialog
import tkinter as tk
from tkinter import *
import os

import src.pembangkitan as pembangkitan, src.Sign as Sign

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomePage(Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Home()

    def Home(self):
        self.canvas = Canvas(
            self.master,
            bg = "#F4F3F9",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        ttk.Label(self.master, text ="Tanda-tangan Digital", font='Helvetika 10 bold').pack()
        ttk.Label(self.master, text ="18220001 Stephanie Hutagalung - 18220002 Verawati Esteria S. Simatupang - 18220010 Agnes Tamara ", font='Helvetika 8').pack()
        self.tabControl = ttk.Notebook(self.master)
        
        tab1 = Frame(self.tabControl)
        tab2 = Frame(self.tabControl)
        tab3 = Frame(self.tabControl)

        self.tabControl.add(tab1, text ='Generator Key')
        self.tabControl.add(tab2, text ='Signing')
        self.tabControl.add(tab3, text ='Verifying')
        self.tabControl.pack(expand = 1, fill ="both")
        
        # tab1
        ttk.Label(tab1, text ="Nama output kunci privat dan publik").grid(sticky='w', column = 0, row = 0, padx = 10, pady = 10)
        self.privatekey = Text(tab1, width=60, height=1, font=("Times New Roman", 10))
        self.privatekey.grid(column = 1, row=0, padx = 10, pady = 10)
        self.b1 = Button(tab1,text="Generate", command=lambda: self.GenerateKey())
        self.b1.grid(row=2, columnspan = 3, pady = 2, padx = 5)       
        
        # tab2
        ttk.Label(tab2, text ="Pilih File").grid(sticky='w',column = 0, row = 0, padx = 10, pady = 10)
        self.stringvar_message = StringVar()
        self.stringvar_message.set("Tidak ada file dipilih")
        self.filemessage = Label(tab2, textvariable = self.stringvar_message)
        self.filemessage.grid(sticky='w', column = 1, row=0, padx = 10, pady = 10)
        self.b2 = Button(tab2,text="Pilih File", command=lambda: self.GetMessage())
        self.b2.grid(row=0, column = 2, pady = 2, padx = 5)        
        ttk.Label(tab2, text ="Kunci Privat").grid(sticky='w', column = 0, row = 1, padx = 10, pady = 10)
        privatekey = LabelFrame(tab2, relief=FLAT)
        ttk.Label(privatekey, text ="d").pack(side = LEFT,  padx=6)
        self.e = Text(privatekey, width=20, height=1, font=("Times New Roman", 10))
        self.e.pack(side = LEFT,  padx=6)
        ttk.Label(privatekey, text ="n").pack(side = LEFT,  padx=6)
        self.n = Text(privatekey, width=20, height=1, font=("Times New Roman", 10))
        self.n.pack(side = LEFT,  padx=6)
        privatekey.grid(sticky='w', column = 1, row = 1, padx = 10, pady = 10)
        self.b3 = Button(tab2,text="Pilih File", command=lambda: self.GetPrivateKey())
        self.b3.grid(row=1, column = 2, pady = 2, padx = 5)  
        self.input = scrolledtext.ScrolledText(tab2, wrap=tk.WORD,width=90, height=8, font=("Times New Roman", 10))
        self.input.grid(sticky="w", row = 2, columnspan = 3, pady = 10, padx = 30)
        ttk.Label(tab2, text ="Tipe Tanda Tangan").grid(sticky='w',column = 0, row = 3, padx = 10, pady = 10)
        self.radio1 = IntVar()
        ttk.Radiobutton(tab2,text="Tanda tangan dalam file", variable=self.radio1, value=1).grid(sticky='w',row=3, column= 1)
        ttk.Radiobutton(tab2,text="Tanda tangan terpisah ", variable=self.radio1, value=2).grid(sticky='w',row=4, column=1)
        self.b4 = Button(tab2,text="Sign", command=lambda: self.Sign())
        self.b4.grid(row=5, columnspan = 3, pady = 2, padx = 5)

        # tab3
        ttk.Label(tab3, text ="Pilih File").grid(sticky='w',column = 0, row = 0, padx = 10, pady = 10)
        self.stringvar_message2 = StringVar()
        self.stringvar_message2.set("Tidak ada file dipilih")
        self.filemessage = Label(tab3, textvariable = self.stringvar_message2)
        self.filemessage.grid(sticky='w', column = 1, row=0, padx = 10, pady = 10)
        self.b2 = Button(tab3,text="Pilih File", command=lambda: self.GetMessage2())
        self.b2.grid(row=0, column = 2, pady = 2, padx = 5)        
        ttk.Label(tab3, text ="Tanda Tangan").grid(sticky='w',column = 0, row = 1, padx = 10, pady = 10)
        self.stringvar_signature = StringVar()
        self.stringvar_signature.set("Tidak ada file dipilih")
        self.filesignature = Label(tab3, textvariable = self.stringvar_signature)
        self.filesignature.grid(sticky='w', column = 1, row=1, padx = 10, pady = 10)
        self.b3 = Button(tab3,text="Pilih File", command=lambda: self.GetSignature())
        self.b3.grid(row=1, column = 2, pady = 2, padx = 5)  
        ttk.Label(tab3, text ="Kunci Publik").grid(sticky='w',column = 0, row = 2, padx = 10, pady = 10)
        publickey = LabelFrame(tab3, relief=FLAT)
        ttk.Label(publickey, text ="p").pack(side = LEFT,  padx=6)
        self.d = Text(publickey, width=20, height=1, font=("Times New Roman", 10))
        self.d.pack(side = LEFT,  padx=6)
        ttk.Label(publickey, text ="n").pack(side = LEFT,  padx=6)
        self.n2 = Text(publickey, width=20, height=1, font=("Times New Roman", 10))
        self.n2.pack(side = LEFT,  padx=6)
        publickey.grid(sticky='w', column = 1, row = 2, padx = 10, pady = 10)
        self.b4 = Button(tab3,text="Pilih File", command=lambda: self.GetPublicKey())
        self.b4.grid(row=2, column = 2, pady = 2, padx = 5)  
        self.input2 = scrolledtext.ScrolledText(tab3, wrap=tk.WORD,width=90, height=8, font=("Times New Roman", 10))
        self.input2.grid(sticky="w", row = 3, columnspan = 3, pady = 10, padx = 30)
        ttk.Label(tab3, text ="Tipe Tanda Tangan").grid(sticky='w',column = 0, row = 4, padx = 10, pady = 10)
        self.radio2 = IntVar()
        ttk.Radiobutton(tab3,text="Tanda tangan dalam file", variable=self.radio2, value=1).grid(sticky='w',row=4, column= 1)
        ttk.Radiobutton(tab3,text="Tanda tangan terpisah ", variable=self.radio2, value=2).grid(sticky='w',row=5, column=1)
        self.b5 = Button(tab3,text="Verivying", command=lambda: self.Verifying())
        self.b5.grid(row=6, columnspan = 3, pady = 2, padx = 5)

    def startPage(self):
        self.mainloop()

    # Generate key
    def GenerateKey(self):
        key = pembangkitan.genPubPrivKey()
        priv = key[0]
        pub = key[1]
        namafile = self.privatekey.get("1.0", "end-1c")
        if namafile == '':
            messagebox.showerror("Error",f"Masukkan nama file")
        else:
            try:
                with open(f"Key/{namafile}.pri", "w") as myfile:
                    myfile.write(f"{priv}")
                with open(f"Key/{namafile}.pub", "w") as myfile:
                    myfile.write(f"{pub}")
                messagebox.showinfo("info", f"Kunci berhasil disimpan di Key/{namafile}.pri dan Key/{namafile}.pub")
            except Exception as E:
                messagebox.showerror("Error",f"Kunci tidak dapat disimpan karena nama file tidak sesuai")

    #Buka Pesan yang akan ditandatangani
    def GetMessage(self):
        try:
            self.filename_message = filedialog.askopenfilename(
                title='Open a file',
                initialdir='File/'
                )
            with open(self.filename_message, 'rb') as f:
                self.fileinput = f.read().decode("latin-1")
            f.close()
            self.input.delete('0.0', tk.END)
            self.input.insert(tk.END, f'{self.fileinput}')
            if len(self.filename_message) > 55:
                # namafile = self.filename_message.split("/")[-2].split[-1]
                namafile = self.filename_message[-55:]
            else:
                namafile = self.filename_message
            self.stringvar_message.set(f'{namafile}')
        except:
            False


    #Buka Pesan yang akan diverifikasi
    def GetMessage2(self):
        try:
            self.filename_message = filedialog.askopenfilename(
                title='Open a file',
                initialdir='File/'
                )
            with open(self.filename_message, 'rb') as f:
                self.fileinput = f.read().decode("latin-1")
            f.close()
            self.input2.delete('0.0', tk.END)
            self.input2.insert(tk.END, f'{self.fileinput}')
            if len(self.filename_message) > 55:
                namafile = self.filename_message[-55:]
            else:
                namafile = self.filename_message
            self.stringvar_message2.set(f'{namafile}')
        except:
            False

    # Buka Signature
    def GetSignature(self):
        try:
            self.filename_signature = filedialog.askopenfilename(
                title='Open a file',
                initialdir='Signature/',
                filetypes =[('Text files', '*.txt')]
                )
            with open(self.filename_signature, 'rb') as f:
                self.fileinput_signature = f.read().decode("latin-1")
            f.close()
            if len(self.filename_signature) > 55:
                namafile = self.filename_signature[-55:]
            else:
                namafile = self.filename_signature
            self.stringvar_signature.set(f'{namafile}')
        except:
            False

    # Buka file pri
    def GetPrivateKey(self):
        try:
            self.filename_key = filedialog.askopenfilename(
                title='Open a file',
                initialdir='Key/',
                filetypes =[('Private key files', '*.pri')]
                )
            with open(self.filename_key, 'rb') as f:
                self.fileinput = f.read().decode("latin-1")
            f.close()
            key = self.fileinput[1:-1]
            E,N = str(key).split(", ")
            self.e.delete('0.0', tk.END)
            self.e.insert(tk.END, f'{int(E)}')
            self.n.delete('0.0', tk.END)
            self.n.insert(tk.END, f'{int(N)}')
        except:
            False

    # Buka file pub
    def GetPublicKey(self):
        try:
            self.filename_key = filedialog.askopenfilename(
                title='Open a file',
                initialdir='Key/',
                filetypes =[('Public key files', '*.pub')]
                )
            with open(self.filename_key, 'rb') as f:
                self.fileinput = f.read().decode("latin-1")
            f.close()
            key = self.fileinput[1:-1]
            D,N = str(key).split(", ")
            self.d.delete('0.0', tk.END)
            self.d.insert(tk.END, f'{int(D)}')
            self.n2.delete('0.0', tk.END)
            self.n2.insert(tk.END, f'{int(N)}')
        except:
            False


    # Sign
    def Sign(self):
        message=''
        PK = ''
        n = ''
        try:
            message = self.input.get("1.0", "end-1c")
            PK = int(self.e.get("1.0", "end-1c"))
            n = int(self.n.get("1.0", "end-1c"))
        except:
            False
        if self.stringvar_message.get() == "Tidak ada file dipilih":
            messagebox.showerror("Error","File yang akan ditandatangani belum dipilih")
        elif PK == '' or n == '':
            messagebox.showerror("Error","Key belum dimasukkan")
        else:
            if self.radio1.get() == 1:
                if ("<DS>" in message) and ("</DS>" in message):
                    messagebox.showerror("Error","Pesan sudah ditandatangani")
                else:
                    if self.filename_message[-3:] == 'txt':
                        signature = Sign.enkrip(message, PK, n)
                        with open(self.filename_message, 'w') as f:
                            mess_sign = f"{message}\n<DS>{signature}</DS>"
                            f.write(mess_sign)
                            self.input.delete('0.0', tk.END)
                            self.input.insert(tk.END, f'{mess_sign}')
                        f.close()
                        messagebox.showinfo("info", "Pesan berhasil ditandatangani")
                    else:
                        messagebox.showerror("Error","Tipe pesan tidak bisa ditandatangani di dalam file")
            elif self.radio1.get() == 2:
                if ("<DS>" in message) and ("</DS>" in message and self.filename_message[-3:] == 'txt'):
                    messagebox.showerror("Error","Pesan sudah ditandatangani")
                else:
                    signature = Sign.enkrip(message, PK, n)
                    namafile = self.filename_message.split("/")[-1].split(".")[0]
                    try:
                        with open(f"Signature/sign_{namafile}.txt", "w") as myfile:
                            myfile.write(f"<DS> {signature} </DS>")
                        messagebox.showinfo("info", f"Signature berhasil disimpan di Signature/sign_{namafile}.txt")
                    except Exception as E:
                        messagebox.showerror("Error",f"Kunci tidak dapat disimpan karena nama file tidak sesuai atau {E}")
            else:
                messagebox.showerror("Error","Tipe Tanda Tangan belum dipilih")

    # verif
    def verif(self, m, PK, n, S):
        verifying = Sign.dekrip(m, PK, n, S)
        if verifying:
            messagebox.showinfo("info", "Tanda tangan valid")
        else:
            messagebox.showerror("Error","Tanda tangan tidak valid")

    # Verifying
    def Verifying(self):
        message=''
        PK = ''
        n = ''
        S = ''
        try:
            message = self.input2.get("1.0", "end-1c")
            PK = int(self.d.get("1.0", "end-1c"))
            n = int(self.n2.get("1.0", "end-1c"))
        except:
            False
        if self.stringvar_message2.get()== "Tidak ada file dipilih":
            messagebox.showerror("Error","File yang sudah ditandatangani belum dipilih")
        elif PK == '' or n == '':
            messagebox.showerror("Error","Key belum dimasukkan")
        else:
            if self.radio2.get() == 1:
                if self.filename_message[-3:] == 'txt':
                    if ("<DS>" in message) and ("</DS>" in message):
                        S2 = message.split("<DS>")[-1].split("</DS>")[0]
                        S = int(message.split("<DS>")[-1].split("</DS>")[0])
                        m = message.replace(f'\n<DS>{S2}</DS>', "").rstrip()
                        self.verif(m, PK, n, S)
                    else:
                        messagebox.showerror("Error","Pesan belum ditandatangani")
                else:
                    messagebox.showerror("Error","Tipe pesan tidak bisa ditandatangani di dalam file") 
            elif self.radio2.get() == 2:
                if self.stringvar_signature.get() == "Tidak ada file dipilih":
                    messagebox.showerror("Error","File yang berisi tanda tangan belum dipilih")
                else:
                    S = int(self.fileinput_signature.split("<DS>")[-1].split("</DS>")[0])
                    self.verif(message, PK, n, S)
            else:
                messagebox.showerror("Error","Tipe Tanda Tangan belum dipilih")