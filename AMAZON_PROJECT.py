import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mc
import os



class Product:
    def __init__(self, name, price, image_path):
        self.name = name
        self.price = price
        self.image_path = image_path

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        return sum(item.price for item in self.items)

class LoginPage:
    
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.master.geometry('800x800')
        self.master.title('Login')
        self.master.configure(bg='')

        
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\vignesh\Desktop\New folder (2)\11.jpg"))
        
        
        self.background_label = tk.Label(self.master, image=self.background_image, bd=0)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        label_font = ('Times new roman', 22)

        
        entry_font = ('Times new roman', 14)

        self.username_label = tk.Label(self.master, text="Username:", bg='cyan',font=label_font)
        self.username_entry = tk.Entry(self.master, font=entry_font, width=20)  

        self.password_label = tk.Label(self.master, text="Password:", bg='cyan',font=label_font)
        self.password_entry = tk.Entry(self.master, show="*", font=entry_font, width=15)

        self.login_button = tk.Button(self.master, text="Login", font=label_font,bg='cyan', command=self.login)

        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button.grid(row=2, column=1, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == 'admin':
            messagebox.showinfo("Login Successful", "Welcome to Amazon Order App!")
            self.app.show_customer_info_page()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

class CustomerInfoPage:
    
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.master.geometry('800x800')
        self.master.title('Customer Information')
        self.master.configure(bg='cyan')

    
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\vignesh\Desktop\New folder (2)\88.jpg"))
        self.background_label = tk.Label(self.master, image=self.background_image, bd=0)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        label_font = ('Times new roman', 22)

        
        entry_font = ('Times new roman', 14)

        self.name_label = tk.Label(self.master, text="Customer Name:", font=label_font)
        self.name_entry = tk.Entry(self.master, font=entry_font)
        self.id_label = tk.Label(self.master, text="Customer ID:", font=label_font)
        self.id_entry = tk.Entry(self.master, font=entry_font)
        self.phone_label = tk.Label(self.master, text="Phone Number:", font=label_font)
        self.phone_entry = tk.Entry(self.master, font=entry_font)
        self.address_label = tk.Label(self.master, text="Address:", font=label_font)
        self.address_entry = tk.Entry(self.master, font=entry_font)
        self.next_button = tk.Button(self.master, text="Next", font=label_font, command=self.next_page)

        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.id_label.grid(row=1, column=0, padx=10, pady=10)
        self.id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.phone_label.grid(row=2, column=0, padx=10, pady=10)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)
        self.next_button.grid(row=4, column=1, padx=10, pady=10)

    def next_page(self):
        customer_name = self.name_entry.get()
        customer_id = self.id_entry.get()
        customer_phone = self.phone_entry.get()
        customer_address = self.phone_entry.get()
        if customer_name and customer_id and customer_phone and customer_address:
            self.app.show_order_page(customer_name, customer_id, customer_phone, customer_address)
        else:
            messagebox.showwarning("Incomplete Information", "Please enter all customer information.")


class OrderPage:
    label_font=('Times new roman',16)
    product_font=('Times new roman',14)
    def __init__(self, master, app, customer_name, customer_id, customer_phone, customer_address):
        self.master = master
        self.app = app
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.customer_product=None

        self.master.geometry('800x800')
        self.master.title('HOME PAGE')
        self.master.configure(bg='cyan')

        
        self.background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\vignesh\Desktop\New folder (2)\5.png"))
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.products = [
            Product("Laptop", 100000, r"C:\Users\vignesh\Desktop\New folder (2)\laptop.png"),
            Product("Smartphone", 50000, r"C:\Users\vignesh\Desktop\New folder (2)\smartphone.jpg"),
            Product("Headphone", 200, r"C:\Users\vignesh\Desktop\New folder (2)\headphones.png"),
            Product("Washing machine", 50000, r"C:\Users\vignesh\Desktop\New folder (2)\washing machine.jpg"),
            Product("Smart TV", 50000, r"C:\Users\vignesh\Desktop\New folder (2)\tv.jpg"),
            
            
            
        ]

        self.shopping_cart = ShoppingCart()

        self.create_widgets()
    def create_widgets(self):
        for i, product in enumerate(self.products):
            product_image = ImageTk.PhotoImage(Image.open(product.image_path).resize((100, 100)))
            
            
            image_label = tk.Label(self.master, image=product_image)
            image_label.grid(row=i, column=0, padx=10, pady=10)

            
            name_price_label = tk.Label(self.master, text=f"{product.name} - Rs{product.price}",font=self.product_font)
            name_price_label.grid(row=i, column=1, padx=10, pady=10)

            
            add_to_cart_button = tk.Button(self.master, text="Add to Cart", font=self.label_font,bg='orange',command=lambda p=product,img=product_image: self.add_to_cart(p))
            add_to_cart_button.grid(row=i, column=2, padx=10, pady=10)

    
        place_order_button = tk.Button(self.master, text="Place Order", font=self.label_font,bg='orange',command=self.place_order)
        place_order_button.grid(row=len(self.products), column=1, padx=10, pady=10)

    
    def add_to_cart(self, product):
        self.customer_product=product
        self.shopping_cart.add_item(product)
        messagebox.showinfo("Added to Cart", f"{product.name} added to your shopping cart.")

    def place_order(self):
        total_amount = self.shopping_cart.calculate_total()
        if total_amount > 0 and self.customer_product:
            
            
            message = f"Order placed for {self.customer_name}.\n"
            message += f"Customer ID: {self.customer_id}\n"
            message += f"Phone Number: {self.customer_phone}\n"
            message += f"Address: {self.customer_address}\n"
            message += f"product name: {self.customer_product.name}\n"
            message += f"Total Amount: Rs{total_amount:.2f}"
            

            messagebox.showinfo("Order Placed", message)
            self.save_to_text_file(message)

            
            self.shopping_cart.items.clear()
            self.app.show_customer_info_page()
        else:
            messagebox.showwarning("Empty Cart", "Your shopping cart is empty. Add products before placing an order.")

        
    def save_to_text_file(self, message,topic="----------BILL INVOICE-----------"):
        
        file_path = r"C:\Users\vignesh\Desktop\amazon.txt"

        
        with open(r"C:\Users\vignesh\Desktop\amazon.txt", "a") as file:
            file.write(f"{topic}:\n")
            file.write(message + "\n")
            
        
    def show(self):
        self.master.deiconify()

class OrderPlacementApp:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x800')
        self.master.title('AMAZON')
        self.master.configure(bg='cyan')

        self.login_page = LoginPage(self.master, self)
        self.customer_info_page = None
        self.order_page = None

    def show_customer_info_page(self):
        if self.customer_info_page is None:
            self.customer_info_page = CustomerInfoPage(self.master, self)

        self.login_page.master.withdraw()
        self.customer_info_page.master.deiconify()

    def show_order_page(self, customer_name, customer_id, customer_phone, customer_address):
        if self.order_page is None:
            self.order_page = OrderPage(self.master, self, customer_name, customer_id, customer_phone, customer_address)

        self.customer_info_page.master.withdraw()
        self.order_page.show()

    def show_login_page(self):
        self.order_page.master.withdraw()
        self.customer_info_page.master.withdraw()
        self.login_page.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderPlacementApp(root)
    root.mainloop()


