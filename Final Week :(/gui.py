import os
import tkinter as tk
from PIL import Image, ImageTk
import requests

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("350x500")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.pages = {}
        for PageClass in (Page1, Page2, Page3):
            page_name = PageClass.__name__
            page = PageClass(parent=self.container, controller=self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")
        self.show_page("Page1")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = tk.StringVar()  # StringVar za čuvanje unetog korisničkog imena
        self.email = tk.StringVar()     # StringVar za čuvanje unete email adrese
        self.image_url = tk.StringVar() # StringVar za čuvanje unete URL adrese slike

        title_label = tk.Label(self, text="Registration Screen", font=('Helvetica', 18))
        title_label.pack(pady=10, padx=10)
        username_label = tk.Label(self, text="Username:", font=('Helvetica', 12))
        username_label.pack(pady=5, padx=10, anchor="w")
        self.username_entry = tk.Entry(self, textvariable=self.username, font=('Helvetica', 12), bd=2)
        self.username_entry.pack(pady=5, padx=10, ipady=3, fill='x')
        email_label = tk.Label(self, text="Email:", font=('Helvetica', 12))
        email_label.pack(pady=5, padx=10, anchor="w")
        self.email_entry = tk.Entry(self, textvariable=self.email, font=('Helvetica', 12), bd=2)
        self.email_entry.pack(pady=5, padx=10, ipady=3, fill='x')
        image_label = tk.Label(self, text="Image URL:", font=('Helvetica', 12))
        image_label.pack(pady=5, padx=10, anchor="w")
        self.image_entry = tk.Entry(self, textvariable=self.image_url, font=('Helvetica', 12), bd=2)
        self.image_entry.pack(pady=5, padx=10, ipady=3, fill='x')
        submit_button = tk.Button(self, text="Register", command=self.register, font=('Helvetica', 12))
        submit_button.pack(pady=10, padx=10, anchor="w")
        login_button = tk.Button(self, text="Login", command=lambda: controller.show_page("Page2"), font=('Helvetica', 12))
        login_button.place(relx=0, rely=0, anchor="nw")

    def register(self):
        # Sačuvaj unete podatke u StringVar objektima
        username = self.username.get()
        email = self.email.get()
        image_url = self.image_url.get()
        print("Username:", username)
        print("Email:", email)
        print("Image URL:", image_url)

        # Prosledi unete podatke na Page3
        user = {'somekey': 'somevalue'}

        x = requests.post(url, json = myobj)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title_label = tk.Label(self, text="Login Screen", font=('Helvetica', 18))
        title_label.pack(pady=10, padx=10)
        username_label = tk.Label(self, text="Username:", font=('Helvetica', 12))
        username_label.pack(pady=5, padx=10, anchor="w")
        self.username_entry = tk.Entry(self, font=('Helvetica', 12), bd=2)
        self.username_entry.pack(pady=5, padx=10, ipady=3, fill='x')
        password_label = tk.Label(self, text="Password:", font=('Helvetica', 12))
        password_label.pack(pady=5, padx=10, anchor="w")
        self.password_entry = tk.Entry(self, font=('Helvetica', 12), bd=2, show="*")
        self.password_entry.pack(pady=5, padx=10, ipady=3, fill='x')
        submit_button = tk.Button(self, text="Login", command=self.login, font=('Helvetica', 12))
        submit_button.pack(pady=10, padx=10, anchor="w")
        registration_button = tk.Button(self, text="Register", command=lambda: controller.show_page("Page1"), font=('Helvetica', 12))
        registration_button.place(relx=0, rely=0, anchor="nw")
        home_button = tk.Button(self, text="Home Page", command=lambda: controller.show_page("Page3"), font=('Helvetica', 12))
        home_button.place(relx=0, rely=0, anchor="nw", y=30)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Login with Username:", username)
        print("Login with Password:", password)
        self.controller.show_page("Page3")

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = tk.StringVar()  # StringVar za prikaz korisničkog imena
        self.email = tk.StringVar()     # StringVar za prikaz email adrese
        self.image_url = tk.StringVar() # StringVar za prikaz URL adrese slike

        title_label = tk.Label(self, text="Home Page", font=('Helvetica', 18))
        title_label.pack(pady=10, padx=10)
        username_label = tk.Label(self, text="Username:", font=('Helvetica', 12))
        username_label.pack(pady=5, padx=10, anchor="w")
        self.username_label = tk.Label(self, textvariable=self.username, font=('Helvetica', 12))
        self.username_label.pack(pady=5, padx=10, anchor="w")
        email_label = tk.Label(self, text="Email:", font=('Helvetica', 12))
        email_label.pack(pady=5, padx=10, anchor="w")
        self.email_label = tk.Label(self, textvariable=self.email, font=('Helvetica', 12))
        self.email_label.pack(pady=5, padx=10, anchor="w")
        image_label = tk.Label(self, text="Slika:", font=('Helvetica', 12))
        image_label.pack(pady=5, padx=10, anchor="w")
        self.image_label = tk.Label(self, textvariable=self.image_url, font=('Helvetica', 12))
        self.image_label.pack(pady=5, padx=10, anchor="w")
        
        registration_button = tk.Button(self, text="Register", command=lambda: controller.show_page("Page1"), font=('Helvetica', 12))
        registration_button.pack(pady=10, padx=10, anchor="w")
        login_button = tk.Button(self, text="Login", command=lambda: controller.show_page("Page2"), font=('Helvetica', 12))
        login_button.pack(pady=10, padx=10, anchor="w")

    def update_data(self, username, email, image_url):
        # Ažuriraj StringVar objekte za prikaz unetih podataka
        self.username.set(username)
        self.email.set(email)
        self.image_url.set(image_url)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
