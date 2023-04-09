from tkinter import Tk
import Home

class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("1280x832")
        self.window.configure(bg = "#F4F3F9")
        self.window.title('Kriptografi dan Koding')
        self.window.resizable(False, False)

        self.page = Home.HomePage(master=self.window, pageManager=self)
    
    def run(self):
        self.page.startPage()
    
    def Home(self):
        self.page = Home.HomePage(master = self.window, pageManager = self)
        self.page.startPage()