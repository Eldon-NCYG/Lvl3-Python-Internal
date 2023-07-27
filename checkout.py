
#Importing all necessary Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image
import random

#Importing all the different pages to the file
import home
import mains
import home
import sides
import checkout
import drinks
from menu_list import shopping_cart_list


global_font = 'roboto'
total_price = 0 

#Setting up Window Properties
class Checkout:
    def __init__(self, root):
        self.root = root

        #Making the window fullscreen
        self.root.state('zoomed')
        
        self.root.title("Wok'n Roll")
        self.root.config(bg = '#F0F0F0')

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
        checkout_canvas = Canvas(self.root, scrollregion=(0,200,2000,len(shopping_cart_list) * 650), width = 200, bg = "#F0F0F0",)
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
        checkout_frame = Frame(checkout_canvas, highlightthickness=0)
        checkout_canvas.create_window((15,200), window = checkout_frame, anchor = "nw")
#================================================================================================================

        global shopping_cart_list_frame
        shopping_cart_list_frame = Frame(checkout_frame, bg = "#F0F0F0",)
        shopping_cart_list_frame.pack(padx = 150)

        shopping_cart_title = Label(shopping_cart_list_frame, text = "Shopping Cart:", font = (global_font, 50), bg = "#F0F0F0", )
        shopping_cart_title.pack(padx = 10, pady = (100, 75))




        #Adding a new item frame for every item that is in the shopping list

        global item_frame_list
        item_frame_list = []
        for item in (shopping_cart_list):
            #Creating the item frame
            global item_frame
            item_frame = Frame(shopping_cart_list_frame, bg = 'white', borderwidth= 20, relief='flat')
            item_frame.pack(pady = 30, fill = 'x', expand = True)
            item_frame.pack_propagate(0)
            
            item_frame_list.append(item_frame)
            #Item image
            image = Image.open(item["item"]["image"]).resize((250, 250), Image.Resampling.LANCZOS)
            image1 = ImageTk.PhotoImage(image)
            item_image = Label(item_frame, image = image1, borderwidth= 0, bg = 'white')
            item_image.image = image1
            item_image.grid(row = 0, column = 0, rowspan = 2)

            #Item title
            item_title = Label(item_frame, text = item["item"]["title"], font= (global_font, 29), bg = "white", width = 18) 
            item_title.grid(row = 0, column = 1, padx = (15, 50), pady = (16,0))

            #Item price
            item_price = Label(item_frame, text = "$" + str(format(item["item"]["price"] * item["quantity"], '.2f')), font = (global_font, 29, 'bold'), bg = 'white', fg = "#F4A72C")
            item_price.grid(row = 1, column = 1, padx = (20,35))

            global total_price
            total_price += item["item"]["price"] * item['quantity']

            #Item Quantity
            item_quantity_title = Label(item_frame, text = "Quantity:", font = (global_font, 29), bg = 'white')
            item_quantity_title.grid(row = 0, column = 2, padx = 15, pady = (16,0))
            item_quantity = Label(item_frame, text = item["quantity"], font = (global_font, 29, "bold"), bg = 'white', fg = "#F4A72C")
            item_quantity.grid(row = 1, column = 2, padx = 15)

            


            #Remove item button (trash)
            bin_image1 = Image.open("Images/bin.png").resize((58, 58), Image.Resampling.LANCZOS)
            bin_image = ImageTk.PhotoImage(bin_image1)
            remove_button = Button(item_frame, image = bin_image, borderwidth= 0, bg = 'white', cursor = 'hand2')

            #Adding event handler when the bin button is clicked
            remove_button.bind("<Button-1>", lambda event, arg = item: remove_item(event, arg))
            remove_button.image = bin_image
            remove_button.grid(row = 0, column = 3, padx = (90,40), pady = 20, rowspan = 2)



        #Last row widgets' frame
        final_frame= Frame(shopping_cart_list_frame, bg = "#F0F0F0")
        final_frame.pack(pady = 35)

        #Total Price
        global total_price_text
        total_price_text = Label(final_frame, text = "Total: $" + str(format(total_price, '.2f')), font= (global_font, 35), bg = "#F0F0F0") 
        total_price_text.grid(row = 0, column = 0)


        #Submit  order button
        submit_image1 = Image.open("Images/submit_order.png").resize((270, 60), Image.Resampling.LANCZOS)
        submit_image = ImageTk.PhotoImage(submit_image1)
        submit_order_button = Button(final_frame, image = submit_image, borderwidth= 0, cursor = 'hand2', bg = "#F0F0F0", command = lambda: self.submit_order())
        submit_order_button.image = submit_image
        submit_order_button.grid(row = 0, column = 1, padx = (80,0))




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


    #Submitting Order 
    def submit_order(self):
        global total_price
        if len(shopping_cart_list) > 0:
            #Confirming user with yes or no
            confirm = messagebox.askquestion(title = None, message = "Confirm Order?")

            #If user presses yes
            if confirm == "yes":
                order_id = random.randint(100,100000)
                messagebox.showinfo(title = "Submission", message = "Your order has been submitted!\nYour order ID is: " + str(order_id))
                
                #Adding order to the list database
                order_list_db = open('order_list_database.txt', 'a')
                
                #Adding an order id
                order_list_db.write("\n\n============================================== Order ID:" + str(order_id) + " ==============================================================================\n")
                
                #Use for loop to add each item in shopping cart
                for item in shopping_cart_list:
                    order_list_db.write(str(item["quantity"]) + "x " + item["item"]["title"] + ": " + "$" + str(format(item["item"]["price"] * item["quantity"], '.2f')) + "\n")
                order_list_db.write("Total Price: $" + str(format(total_price, '.2f')))
                order_list_db.write("\n==========================================================================================================================================\n")
                
                #Removing all items from shopping cart and resetting total price
                shopping_cart_list.clear()
                for item in item_frame_list:
                    item.destroy()

                total_price = 0
                total_price_text.config(text = "Total: $" + str(format(total_price, '.2f')))
                
            else:
                pass
        else:
            messagebox.showerror(title = None, message = "You don't have anything in your shopping cart!")


#Clicking on Bin removes item frame and item from the shopping cart list
def remove_item(item_widget, item):
    global total_price
    #Confirming user with yes or no
    confirm = messagebox.askquestion('Remove item', "Are you sure you want to remove " + str(item["quantity"]) + "x " + item["item"]["title"] + "?")

    #If user presses yes
    if confirm == "yes":
        #Removing item's frame
        item_widget = item_widget.widget
        remove_item_frame = item_widget.master
        remove_item_frame.destroy()


        #Removing from shopping cart list 
        shopping_cart_list.remove(item)

        #Updating total price
        total_price -= item["item"]["price"] * item["quantity"]
        total_price_text.config(text = "Total: $" + str(format(total_price, '.2f')))
    
    #If the user presses no
    else:
        pass



#Displaying the current page on the tkinter root window
def page():
    root = Tk()
    Checkout(root)
    root.mainloop()
if __name__ == '__main__':
    page()  





