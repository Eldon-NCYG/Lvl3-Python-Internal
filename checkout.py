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
from menu_list import mains_menu_list


global_font = 'roboto'
shopping_cart_list = []



#Setting up Window Properties
class Checkout:
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


        #Shopping Cart Button at the bottom of menu bar
        checkout_image = Image.open("Images\checkout.png")
        checkout_photo = ImageTk.PhotoImage(checkout_image)
        menu_bar_checkout = Button(menu_bar_frame, image = checkout_photo, bg = "white", borderwidth=0, cursor = "hand2", command = lambda: self.change_page("checkout"))
        menu_bar_checkout.image = checkout_photo
        menu_bar_checkout.pack(anchor='s', side = 'left', padx = 20, pady = 20)

        # #Page indicator that shows a small orange box next to the currently opened page of the program (refinement based on stakeholder feedback)
        # page_indicator = Label(menu_bar_frame, text = '', bg ='#F4A72C', width = 103)
        # page_indicator.pack(anchor='s', side = 'left', pady= 20, padx = (0, 20))

#================================================Sidebar End======================================================

    #================================================Checkout start======================================================

#==========================================Adding scrollbars=================================================
        #checkout canvas containing all home page widgets
        checkout_canvas = Canvas(self.root, scrollregion=(0,200,1800,2000), width = 200, bg = "#F5F5F5")
        checkout_canvas.pack(fill = 'both', expand = True)

        #Adding a Vertical Scrollbar
        checkout_canvas.bind_all('<MouseWheel>', lambda event: checkout_canvas.yview_scroll(-int(event.delta / 100), "units"))
        yscrollbar = ttk.Scrollbar(self.root, orient = 'vertical', command = checkout_canvas.yview)
        checkout_canvas.configure(yscrollcommand= yscrollbar.set)
        checkout_canvas.configure(scrollregion=checkout_canvas.bbox('all'))
        yscrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')


        #Adding a horizontal scrollbar
        checkout_canvas.bind_all('<Control MouseWheel>', lambda event: checkout_canvas.xview_scroll(-int(event.delta / 100), "units"))
        xscrollbar = ttk.Scrollbar(self.root, orient = 'horizontal', command = checkout_canvas.xview)
        checkout_canvas.configure(xscrollcommand=xscrollbar.set)
        checkout_canvas.configure(scrollregion=checkout_canvas.bbox('all'))
        xscrollbar.place(relx = 0, rely = 1, relwidth=1, anchor = 'sw')

        #Creating new home_page_frame contianing the scrollbar (weird feature that is required for the code to work)
        checkout_frame = Frame(checkout_canvas)
        checkout_canvas.create_window((15,200), window = checkout_frame, anchor = "nw")
#================================================================================================================

        shopping_cart_list_frame = Frame(checkout_frame)
        shopping_cart_list_frame.pack()

        shopping_cart_title = Label(shopping_cart_list_frame, text = "Shopping Cart", font = (global_font, 25))
        shopping_cart_title.pack(padx = 50, pady = 50)

        for item in shopping_cart_list:
            item_frame = Frame(shopping_cart_list_frame, bg = 'white')
            item_frame.pack()

            item_title = Label(item_frame, text = item["name"], font= (global_font, 12), bg = "white") 
            item_title.grid(row = 0, column = 2)





#================================================checkout End======================================================

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
    Checkout(root)
    root.mainloop()
if __name__ == '__main__':
    page()  





