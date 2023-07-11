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




#Dish_Viewer Class Window
class Dish_Viewer:
    def __init__(self, root, dish, previous_page):
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
        page_indicator.place(x = 42, y = 253)

        #Shopping Cart Button at the bottom of menu bar
        checkout_image = Image.open("Images\checkout.png")
        checkout_photo = ImageTk.PhotoImage(checkout_image)
        menu_bar_checkout = Button(menu_bar_frame, image = checkout_photo, bg = "white", borderwidth=0, cursor = "hand2", command = lambda: self.change_page("checkout"))
        menu_bar_checkout.image = checkout_photo
        menu_bar_checkout.pack(anchor='s', side = 'left', padx = 20, pady = 20)

    #======================================Menu sidebar end========================================

    #==================================================Dish Viewer Window Setup=============================================

        #dish viewer canvas page canvas containing all home page widgets
        dish_viewer_canvas = Canvas(self.root, scrollregion=(0,0,1700,900), width = 200, bg = "#F5F5F5")
        dish_viewer_canvas.pack(fill = 'both', expand = True)

        #Adding a Vertical Scrollbar
        dish_viewer_canvas.bind_all('<MouseWheel>', lambda event: dish_viewer_canvas.yview_scroll(-int(event.delta / 100), "units"))
        yscrollbar = ttk.Scrollbar(self.root, orient = 'vertical', command = dish_viewer_canvas.yview)
        dish_viewer_canvas.configure(yscrollcommand= yscrollbar.set)
        dish_viewer_canvas.configure(scrollregion=dish_viewer_canvas.bbox('all'))
        yscrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')


        #Adding a horizontal scrollbar
        dish_viewer_canvas.bind_all('<Control MouseWheel>', lambda event: dish_viewer_canvas.xview_scroll(-int(event.delta / 100), "units"))
        xscrollbar = ttk.Scrollbar(self.root, orient = 'horizontal', command = dish_viewer_canvas.xview)
        dish_viewer_canvas.configure(xscrollcommand=xscrollbar.set)
        dish_viewer_canvas.configure(scrollregion=dish_viewer_canvas.bbox('all'))
        xscrollbar.place(relx = 0, rely = 1, relwidth=1, anchor = 'sw')

        #Creating new home_page_frame contianing the scrollbar (weird feature that is required for the code to work)
        dish_viewer_frame = Frame(dish_viewer_canvas, bg = '#F5F5F5', highlightbackground='#F5F5F5')
        dish_viewer_canvas.create_window((15,60), window = dish_viewer_frame, anchor = "nw")

    #====================================Dish Viewer Window setup end ==============================================================


#============================Dish Viewer==================================================================

        #frame for the dish profile (Using grid to position the widgets involved)
        dish_profile = Frame(dish_viewer_frame, bg = '#F5F5F5', borderwidth=60, relief='flat', width = 1700)
        dish_profile.pack(anchor = 'center', padx = (80, 10))

        back_button_image1 = Image.open("Images/back.png").resize((50,50), Image.Resampling.LANCZOS)
        back_button_image = ImageTk.PhotoImage(back_button_image1)
        back_button = Button(dish_viewer_frame, image = back_button_image, bg = '#F5F5F5', borderwidth=0, cursor = 'hand2', command = lambda: self.change_page(previous_page))
        back_button.image = back_button_image
        back_button.place(x = 55, y = 0)

        #Large Dish title
        dish_title = Label(dish_profile, text = dish["title"], bg ='#F5F5F5', font = ("Helvetica", 48))
        dish_title.grid(column = 0, row = 0, padx = 40, pady = (25,60), columnspan=2)

        #Dish Imgae on the right
        dish_image1 = Image.open(dish["image"]).resize((600, 620), Image.Resampling.LANCZOS)
        dish_photo = ImageTk.PhotoImage(dish_image1)
        dish_image = Label(dish_profile, image = dish_photo, borderwidth= 0, bg = 'white')
        dish_image.image = dish_photo
        dish_image.grid(row = 0, column = 2, rowspan = 4, padx = 100)

        #Dish price
        dish_price = Label(dish_profile, text = "$" + str(format(dish["price"], '.2f')), fg ='#C87E07', bg = "#F5F5F5", font = (global_font, 23))
        dish_price.grid(column = 0, row = 1, padx =(0, 150))

        #Dish rating + random number of ratings for decorational purposes
        dish_rating = Label(dish_profile, text = str(dish["rating"]) + "/10 (" + str(random.randint(0,1000)) + " ratings)", bg ='#F5F5F5', font = (global_font, 23))
        dish_rating.grid(column = 1, row = 1,padx = (0,20))

        #Bold description title
        dish_description_title = Label(dish_profile, text = "Description:", bg ='#F5F5F5', font = (global_font, 25, 'bold'), anchor = 'w', justify='left')
        dish_description_title.grid(column = 0, row = 2, columnspan=2, pady = (40, 3), padx = (0, 450))
        
        #Dish description
        dish_description = Label(dish_profile, text = dish["description"], bg ='#F5F5F5', font = (global_font, 18), anchor = 'w', justify='left')
        dish_description.bind('<Configure>', lambda e: dish_description.config(wraplength = 650 ))
        dish_description.grid(column = 0, row = 3, rowspan=2, columnspan = 2)

        #Add to cart button
        add_to_cart_image1 = Image.open("Images/add_to_cart.png").resize((250,60), Image.Resampling.LANCZOS)
        add_to_cart_image = ImageTk.PhotoImage(add_to_cart_image1)
        add_to_cart_button = Button(dish_profile, image = add_to_cart_image, bg = '#F5F5F5', borderwidth=0, cursor = 'hand2',)
        add_to_cart_button.image = add_to_cart_image
        add_to_cart_button.grid(column = 2, row = 5, rowspan=4,pady = 25)
#=====================================dish viewer==================================================================================



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
    Dish_Viewer(root)
    root.mainloop()
if __name__ == '__main__':
    page()





