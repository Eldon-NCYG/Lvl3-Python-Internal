from tkinter import *
from PIL import ImageTk, Image

#Setting up Window Properties
root = Tk()
root.geometry("1000x600")
root.title("Wok'n Roll")
root.config(bg = '#F5F5F5')

#Making window unresizable to that the widgets are messed up if the window is resized
root.resizable(False, False)





#=========================================Side Menu Bar=============================================

#Side menu bar frame
menu_bar_frame = Frame(root, bg = 'white')
menu_bar_frame.pack(side = LEFT)
menu_bar_frame.pack_propagate(False)
menu_bar_frame.configure(width = 213, height = 720)

#Menubar logo image
logo_image1 = Image.open("Images\logo.png")
logo_image = ImageTk.PhotoImage(logo_image1)
menu_bar_logo = Label(root, image = logo_image, cursor = "hand2")
menu_bar_logo.place(x = 0, y = 0)


#Menu bar options for home, mains, sides, and drinks
home_page = Button(menu_bar_frame, text = 'Home', font = ('roboto', 20), bg = 'white', bd = 0, cursor = "hand2")
home_page.place(x = 45, y = 120)
mains_page = Button(menu_bar_frame, text = 'Mains', font = ('roboto', 20), bg = 'white', bd = 0, cursor = "hand2")
mains_page.place(x = 45, y = 195)
sides_page = Button(menu_bar_frame, text = 'Sides', font = ('roboto', 20), bg = 'white', bd = 0, cursor = "hand2")
sides_page.place(x = 45, y = 270)
drinks_page = Button(menu_bar_frame, text = 'Drinks', font = ('roboto', 20), bg = 'white', bd = 0, cursor = "hand2")
drinks_page.place(x = 45, y =345)


#Shopping Cart Button at the bottom of menu bar
checkout_image1 = Image.open("Images\checkout.png")
checkout_image = ImageTk.PhotoImage(checkout_image1)
menu_bar_checkout = Label(root, image = checkout_image, bg = "white", cursor = "hand2")
menu_bar_checkout.place(x = 20, y = 520)











root.mainloop()