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


#Font that will be used throughout the program
global_font = 'roboto'

#Setting up Window Properties
class Home:
    def __init__(self, root):
        self.root = root

        #Making the window fullscreen
        self.root.state('zoomed')

        self.root.title("Wok'n Roll")
        self.root.config(bg = '#F0F0F0')

        #Making minimum available window size
        self.root.minsize(1250,600)
        self.root.maxsize(1920,1080)



#=========================================Side Menu Bar=============================================

        #Side menu bar home_page_frame
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
        page_indicator.place(x = 42, y = 168)


        #Shopping Cart Button at the bottom of menu bar
        checkout_image = Image.open("Images\checkout.png")
        checkout_photo = ImageTk.PhotoImage(checkout_image)
        menu_bar_checkout = Button(menu_bar_frame, image = checkout_photo, bg = "white", borderwidth=0, cursor = "hand2", command = lambda: self.change_page("checkout"))
        menu_bar_checkout.image = checkout_photo
        menu_bar_checkout.pack(anchor='s', side = 'left', padx = 20, pady = 20)

    #======================================Menu sidebar end========================================

    #==================================================Adding Scrollbars=============================================
        #Home page canvas containing all home page widgets
        home_page_canvas = Canvas(self.root, scrollregion=(0,0,1707,1080))
        home_page_canvas.pack(fill = 'both', expand = True)

        #Adding a Vertical Scrollbar
        home_page_canvas.bind_all('<MouseWheel>', lambda event: home_page_canvas.yview_scroll(-int(event.delta / 100), "units"))
        yscrollbar = ttk.Scrollbar(self.root, orient = 'vertical', command = home_page_canvas.yview)
        home_page_canvas.configure(yscrollcommand= yscrollbar.set)
        home_page_canvas.configure(scrollregion=home_page_canvas.bbox('all'))
        yscrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')


        #Adding a horizontal scrollbar
        home_page_canvas.bind_all('<Control MouseWheel>', lambda event: home_page_canvas.xview_scroll(-int(event.delta / 100), "units"))
        xscrollbar = ttk.Scrollbar(self.root, orient = 'horizontal', command = home_page_canvas.xview)
        home_page_canvas.configure(xscrollcommand=xscrollbar.set)
        home_page_canvas.configure(scrollregion=home_page_canvas.bbox('all'))
        xscrollbar.place(relx = 0, rely = 1, relwidth=1, anchor = 'sw')

        #Creating new home_page_frame contianing the scrollbar (weird feature that is required for the code to work)
        home_page_frame = Frame(home_page_canvas)
        home_page_canvas.create_window((0,0), window = home_page_frame, anchor = "nw")

#===========================================================================================================================

#==================================================Homepage================================================================
        #Homepage title/logo
        home_page_logo_image1 = Image.open("Images\wokn-roll-low-resolution-logo-color-on-transparent-background (1).png")
        home_page_logo_image1 = home_page_logo_image1.resize((500, 150))
        home_page_logo_image = ImageTk.PhotoImage(home_page_logo_image1)
        home_page_logo = Label(home_page_frame, image = home_page_logo_image, borderwidth= 5)
        home_page_logo.image = home_page_logo_image
        home_page_logo.pack(anchor = 'c', pady = 45)

        #Homepage about description
        home_page_about = Label(home_page_frame, text = "Welcome to our authentic Chinese restaurant, where we take pride in serving you a delightful culinary experience steeped in the rich traditions of Chinese cuisine. ", bg = 'white', font = (global_font, 30), width = 65, height = 4, borderwidth = 10)
        home_page_about.bind('<Configure>', lambda e: home_page_about.config(wraplength = home_page_about.winfo_width()))
        home_page_about.pack(padx = 60, pady = 25)


        #Daily Special Dish Section

        #Randomly selecting a special dish from the mains menu
        special_dish = random.choice(mains_menu_list)

        home_page_specials = Frame(home_page_frame, bg = 'white', height = 450, )
        home_page_specials.pack(anchor = 'center', pady = 65)
        home_page_specials.pack_propagate(False)

        #Special Dish Image
        special_image = Image.open(special_dish["image"]).resize((375,375))
        special_photo = ImageTk.PhotoImage(special_image)
        special_dish_image = Label(home_page_specials, image = special_photo, bg = "white", borderwidth=0)
        special_dish_image.image = special_photo
        special_dish_image.grid(row = 0, column = 0, rowspan=3)


        #Today's Special 
        todays_special = Label(home_page_specials, text = "TODAY'S SPECIAL:", font = (global_font, 40, "bold"),fg = "#C87E07", bg = 'white')
        todays_special.grid(row = 0, column = 1, padx = 105)

        special_dish_title_price = Label(home_page_specials, text = special_dish["title"] + ": $" + str(format(special_dish["price"]/2, '.2f')), font = (global_font, 35), bg = 'white')
        special_dish_title_price.grid(row = 1, column = 1)

        #SPecial dish price (formating to two decimal points for the price)
        special_dish_discount = Label(home_page_specials, text = "(50% off!)", font = (global_font , 40, "bold"), bg = 'white')
        special_dish_discount.grid(row =2, column = 1)


    #==================================================Homepage end=============================================


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
    Home(root)
    root.mainloop()
if __name__ == '__main__':
    page()





