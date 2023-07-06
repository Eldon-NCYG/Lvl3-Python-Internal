from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
import random


#Importing all the different pages to the file
import home
import mains
import home
import sides
import checkout
import drinks
from menu_list import drinks_menu_list

global_font = 'roboto'

#Setting up Window Properties
class Drinks:
    def __init__(self, root):
        self.root = root

        #Making the window fullscreen
        self.root.state('zoomed')

        self.root.title("Wok'n Roll")
        self.root.config(bg = '#F5F5F5')

        #Making minimum available window size
        self.root.minsize(1250,600)




    #=========================================Side Menu Bar=============================================

        #Side menu bar frame
        menu_bar_frame = Frame(self.root, bg = 'white')
        menu_bar_frame.pack(side = LEFT)
        menu_bar_frame.pack_propagate(False)
        menu_bar_frame.configure(width = 213, height = 2000)

        #Menubar logo image
        logo_image1 = Image.open("Images\logo.png")
        logo_image = ImageTk.PhotoImage(logo_image1)
        menu_bar_logo = Button(self.root, image = logo_image, cursor = "hand2", borderwidth= 0, bg = 'white', command = lambda: self.change_page("home"))
        menu_bar_logo.image = logo_image
        menu_bar_logo.place(x = 0, y = 20)


        #Menu bar options for home, mains, sides, and drinks
        home_page = Button(menu_bar_frame, text = 'Home', font = (global_font, 21), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("home"))
        home_page.place(x = 52, y = 160)
        mains_page = Button(menu_bar_frame, text = 'Mains', font = (global_font, 21), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("mains"))
        mains_page.place(x = 52, y = 245)
        sides_page = Button(menu_bar_frame, text = 'Sides', font = (global_font, 21), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("sides"))
        sides_page.place(x = 52, y = 330)
        drinks_page = Button(menu_bar_frame, text = 'Drinks', font = (global_font, 21), bg = 'white', bd = 0, cursor = "hand2", command = lambda: self.change_page("drinks"))
        drinks_page.place(x = 50, y =415)

        #Page indicator that shows a small orange box next to the currently opened page of the program
        page_indicator = Label(menu_bar_frame, text = '', bg ='#F4A72C', height = 2)
        page_indicator.place(x = 42, y = 423)


        #Shopping Cart Button at the bottom of menu bar
        checkout_image = Image.open("Images\checkout.png")
        checkout_photo = ImageTk.PhotoImage(checkout_image)
        menu_bar_checkout = Button(menu_bar_frame, image = checkout_photo, bg = "white", borderwidth=0, cursor = "hand2", command = lambda: self.change_page("checkout"))
        menu_bar_checkout.image = checkout_photo
        menu_bar_checkout.pack(anchor='s', side = 'left', padx = 20, pady = 20)

#======================================Menu sidebar end========================================

#==========================================Drinks Page=================================================
        #Home page canvas containing all home page widgets
        drinks_page_canvas = Canvas(self.root, scrollregion=(0,0,1800,2000), width = 200, bg = "#F5F5F5")
        drinks_page_canvas.pack(fill = 'both', expand = True)

        #Adding a Vertical Scrollbar
        drinks_page_canvas.bind_all('<MouseWheel>', lambda event: drinks_page_canvas.yview_scroll(-int(event.delta / 100), "units"))
        yscrollbar = ttk.Scrollbar(self.root, orient = 'vertical', command = drinks_page_canvas.yview)
        drinks_page_canvas.configure(yscrollcommand= yscrollbar.set)
        drinks_page_canvas.configure(scrollregion=drinks_page_canvas.bbox('all'))
        yscrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')


        #Adding a horizontal scrollbar
        drinks_page_canvas.bind_all('<Control MouseWheel>', lambda event: drinks_page_canvas.xview_scroll(-int(event.delta / 100), "units"))
        xscrollbar = ttk.Scrollbar(self.root, orient = 'horizontal', command = drinks_page_canvas.xview)
        drinks_page_canvas.configure(xscrollcommand=xscrollbar.set)
        drinks_page_canvas.configure(scrollregion=drinks_page_canvas.bbox('all'))
        xscrollbar.place(relx = 0, rely = 1, relwidth=1, anchor = 'sw')

        #Creating new home_page_frame contianing the scrollbar (weird feature that is required for the code to work)
        drinks_page_frame = Frame(drinks_page_canvas)
        drinks_page_canvas.create_window((40,200), window = drinks_page_frame, anchor = "nw")

        #Mains Menu Lists 
        drinks_title_image1 = Image.open("Images/menu items/drinks/drinks_title.png")
        drinks_title_image = ImageTk.PhotoImage(drinks_title_image1)
        drinks_page_title = Label(drinks_page_canvas, image = drinks_title_image, width = 2000, height = 175, bg ="#F5F5F5")
        drinks_page_title.image = drinks_title_image
        drinks_page_title.pack(anchor = 'center')

        menu_list_frame = Frame(drinks_page_frame, bg = '#F5F5F5')
        menu_list_frame.pack(anchor = 'center')

        #Row and column counter for grid manipulation
        row_counter = 0
        column_counter = 0

        #Adding an item frame for each item in the main menu list
        for item in drinks_menu_list:

            #Creating the frame
            item_frame = Frame(menu_list_frame, bg = 'white', borderwidth= 20, relief='flat')

            #Using grid to have a 3 column layout of the menu list
            item_frame.grid(column = column_counter, row = row_counter, padx = 30, pady = 25)
            column_counter +=1

            if column_counter%4 == 0:
                row_counter +=1
                column_counter = 0


            #Item image
            dish_image2 = Image.open(item["image"]).resize((300,315), Image.ANTIALIAS)
            dish_image1 = ImageTk.PhotoImage(dish_image2)
            dish_image = Label(item_frame, image = dish_image1, borderwidth = 0, bg = 'white')
            dish_image.image = dish_image1
            dish_image.grid(row = 0, column = 0, columnspan=2)


            #Item title
            item_title = Label(item_frame, text = item["title"], font = (global_font, 25), bg = "white")
            item_title.grid(row = 1, column = 0, columnspan = 2, pady = 15)

            #Item price  
            item_price = Label(item_frame, text = "$" + str(format(item["price"], '.2f')), fg = "#C87E07", bg = "white", font = (global_font, 22, "bold"))
            item_price.grid(row = 2, column = 0, pady =(5, 12))

            #View Item
            drinks_add_to_cart_button_image1 = Image.open("Images/menu items/drinks/drinks_add_to_cart.png").resize((140, 35), Image.ANTIALIAS)
            drinks_add_to_cart_button_image = ImageTk.PhotoImage(drinks_add_to_cart_button_image1)
            drinks_add_to_cart = Button(item_frame, image = drinks_add_to_cart_button_image, borderwidth = 0, bg = 'white')
            drinks_add_to_cart.image = drinks_add_to_cart_button_image
            drinks_add_to_cart.grid(row = 2, column = 1, pady = (5,12))



#===================================Drinks Page End==============================================

#Navitating around the different pages of the program
    def change_page(self, page):
        win = Toplevel()
        if page == 'home':
            home.Home(win)
        elif page == 'mains':
            mains.Mains(win)
        elif page == 'sides':
            sides.Sides(win)
        elif page == 'drinks':
            drinks.Drinks(win)
        elif page == 'checkout':
            checkout.Checkout(win)
        self.root.withdraw()

#Displaying the current page on the tkinter root window
def page():
    root = Tk()
    Drinks(root)
    root.mainloop()
if __name__ == '__main__':
    page()





