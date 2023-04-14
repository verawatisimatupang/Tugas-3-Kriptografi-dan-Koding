from tkinter import Tk
import src.Home as Home

class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("650x420")
        self.window.configure(bg = "#FFFFFF")
        self.window.title('Kriptografi dan Koding')
        self.window.resizable(False, False)

        self.page = Home.HomePage(master=self.window, pageManager=self)
    
    def run(self):
        self.page.startPage()
    
    def Home(self):
        self.page = Home.HomePage(master = self.window, pageManager = self)
        self.page.startPage()