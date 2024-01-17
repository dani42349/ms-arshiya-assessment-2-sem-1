import requests
import tkinter as tk
from tkinter import messagebox

class CountryInfoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Country Information App")

        
        self.pages = {}

        
        self.create_search_page()
        self.create_instructions_page()

        
        self.show_page("Search")

    def create_search_page(self):
        search_frame = tk.Frame(self.root)

        
        label = tk.Label(search_frame, text="Enter country name:")
        label.pack(pady=10)

        entry = tk.Entry(search_frame)
        entry.pack(pady=10)

        search_button = tk.Button(search_frame, text="Search", command=lambda: self.search_country(entry.get()))
        search_button.pack(pady=10)

        self.pages["Search"] = search_frame

    def create_instructions_page(self):
        instructions_frame = tk.Frame(self.root)

        
        instructions_text = "Welcome to the Country Information App!\n\n"\
                            "1. Enter a country name and click 'Search' to get information.\n"\
                            "2. Use the 'Instructions' button to view this page.\n"\
                            "3. Explore other options for more functionality."
        instructions_label = tk.Label(instructions_frame, text=instructions_text, justify="left")
        instructions_label.pack(pady=10)

        self.pages["Instructions"] = instructions_frame

    def show_page(self, page_name):
        
        for page in self.pages.values():
            page.pack_forget()

        
        self.pages[page_name].pack()

    def search_country(self, country_name):
        if not country_name:
            messagebox.showwarning("Input Error", "Please enter a country name.")
            return

        try:
            
            response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
            data = response.json()

            
            country_data = data[0]

            capital = country_data['capital']
            population = country_data['population']
            languages = ', '.join(country_data['languages'].values())

            
            result_text = f"Capital: {capital}\nPopulation: {population}\nLanguages: {languages}"
            messagebox.showinfo("Country Information", result_text)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to retrieve data: {e}")

if _name_ == "_main_":
    root = tk.Tk()
    app = CountryInfoApp(root)
    root.mainloop()