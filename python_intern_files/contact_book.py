import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300+300+300")
        self.root.maxsize(400,400)
        self.root.minsize(150,200)
        self.root.title("Contact Book")
        self.root.configure(background="lavender")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Name:",background="lavender",)
        self.label_name.grid(row=0, column=4, padx=5, pady=5,)

        self.entry_name = tk.Entry(self.root,background="lavender")
        self.entry_name.grid(row=0, column=5, padx=5, pady=5,)

        self.label_phone = tk.Label(self.root, text="Phone:",background="lavender")
        self.label_phone.grid(row=1, column=4, padx=5, pady=5)

        self.entry_phone = tk.Entry(self.root,background="lavender")
        self.entry_phone.grid(row=1, column=5, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Contact",background="lavender", command=self.add_contact)
        self.add_button.grid(row=2, column=4, columnspan=2, padx=5, pady=5, sticky="we")

        self.view_button = tk.Button(self.root, text="View Contacts",background="lavender", command=self.view_contacts)
        self.view_button.grid(row=3, column=5, columnspan=2, padx=5, pady=5, sticky="we")

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact,background="lavender")
        self.delete_button.grid(row=4, column=4, columnspan=2, padx=5, pady=5, sticky="we")

        self.update_button = tk.Button(self.root, text="Update Contact",background="lavender", command=self.update_contact)
        self.update_button.grid(row=5, column=5, columnspan=2, padx=5, pady=5, sticky="we")

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if name and phone:
            self.contacts.append((name, phone))
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def delete_contact(self):
        name = self.entry_name.get()

        for contact in self.contacts:
            if contact[0] == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully.")
                self.clear_entries()
                return

        messagebox.showerror("Error", "Contact not found.")

    def update_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        for i, contact in enumerate(self.contacts):
            if contact[0] == name:
                self.contacts[i] = (name, phone)
                messagebox.showinfo("Success", "Contact updated successfully.")
                self.clear_entries()
                return

        messagebox.showerror("Error", "Contact not found.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"Name: {contact[0]}, Phone: {contact[1]}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()