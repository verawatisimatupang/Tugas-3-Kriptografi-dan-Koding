from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomePage(Tk.Frame):
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
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("ttd_button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("ttd_button_1 clicked"),
            relief="flat"
        )
        self.ttd_button_1.place(
            x=462.0,
            y=437.0,
            width=356.0,
            height=76.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("verifikasi_button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("verifikasi_button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=462.0,
            y=555.0,
            width=356.0,
            height=76.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("kunci_button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("kunci_button_3 clicked"),
            relief="flat"
        )
        self.kunci_button_3.place(
            x=462.0,
            y=319.0,
            width=356.0,
            height=76.0
        )

        self.canvas.create_text(
            213.0,
            158.0,
            anchor="nw",
            text="by :\nStephanie Hutagalung, Verawati Esteria S. Simatupang, Agnes Tamara",
            fill="#000000",
            font=("OpenSansItalic Regular", 20 * -1)
        )

        self.canvas.create_text(
            579.0,
            55.0,
            anchor="nw",
            text="RSA",
            fill="#000000",
            font=("OpenSansRoman Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()
    
    def click_pembangkitan_kunci(self):
        self.origin.PembangkitanKunci()
    
    def click_pembangkitan_ttd(self):
        self.origin.PembangkitanTTD()
    
    def click_verifikasi_ttd(self):
        self.origin.VerifikasiTTD()