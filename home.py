from tkinter import *
from PIL import ImageTk, Image

#Importing all the different pages to the file
import home
import mains
import home
import sides
import checkout
import drinks


global_font = 'roboto'

#Setting up Window Properties
class Home:
  def __init__(self, root):
    self.root = root
    self.root.geometry("1000x600")
    self.root.title("Wok'n Roll")
    self.root.config(bg = '#F5F5F5')

    #Making window unresizable to that the widgets are messed up if the window is resized
    self.root.resizable(False, False)



#=========================================Side Menu Bar=============================================

    #Side menu bar frame
    menu_bar_frame = Frame(self.root, bg = 'white')
    menu_bar_frame.pack(side = LEFT)
    menu_bar_frame.pack_propagate(False)
    menu_bar_frame.configure(width = 213, height = 720)

    #Menubar logo image
    logo_image1 = Image.open("Images\logo.png")
    logo_image = ImageTk.PhotoImage(logo_image1)
    menu_bar_logo = Label(self.root, image = logo_image, cursor = "hand2")
    menu_bar_logo.image = logo_image
    menu_bar_logo.place(x = 0, y = 0)


    #Menu bar options for home, mains, sides, and drinks
    home_page = Button(menu_bar_frame, text = 'Home', font = (global_font, 20), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("home"))
    home_page.place(x = 45, y = 120)
    mains_page = Button(menu_bar_frame, text = 'Mains', font = (global_font, 20), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("mains"))
    mains_page.place(x = 45, y = 195)
    sides_page = Button(menu_bar_frame, text = 'Sides', font = (global_font, 20), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("sides"))
    sides_page.place(x = 45, y = 270)
    drinks_page = Button(menu_bar_frame, text = 'Drinks', font = (global_font, 20), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("drinks"))
    drinks_page.place(x = 45, y =345)


    #Shopping Cart Button at the bottom of menu bar
    checkout_image = Image.open("Images\checkout.png")
    checkout_photo = ImageTk.PhotoImage(checkout_image)
    menu_bar_checkout = Button(self.root, image = checkout_photo, bg = "white", cursor = "hand2", command = lambda: self.change_page("checkout"))
    menu_bar_checkout.image = checkout_photo
    menu_bar_checkout.place(x = 20, y = 520)

#======================================Menu sidebar end========================================

#==================================================Homepage=============================================

    home_page_title = Label(self.root, text = "Home", font = (global_font, 20))
    home_page_title.place(x = 400, y = 20)

  def change_page(self, page):
    win = Toplevel()
    if page == 'home':
      home.Home(win)
    elif page == 'mains':
      mains.Mains(win)
    elif page == 'sides':
      sides.Sides(win)
    elif page == 'drinks':
      drinks.Drinks
    elif page == 'checkout':
      checkout.Checkout
    self.root.withdraw()

def page():
  root = Tk()
  Home(root)
  root.mainloop()


if __name__ == '__main__':
  page()





