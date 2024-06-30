import customtkinter as ctk
from tkinter import messagebox

# Initialize the application window
app = ctk.CTk()
app.title("Contact Book")
app.geometry("600x400")

contacts = {}

# Functions to handle contacts
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        entry_name.delete(0, ctk.END)
        entry_phone.delete(0, ctk.END)
        entry_email.delete(0, ctk.END)
        entry_address.delete(0, ctk.END)
        messagebox.showinfo("Success", "Contact added successfully!")
        display_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def display_contacts():
    for widget in frame_contact_list.winfo_children():
        widget.destroy()
        
    for name, details in contacts.items():
        contact_frame = ctk.CTkFrame(frame_contact_list)
        contact_frame.pack(pady=5, fill="x", padx=5)
        
        label_name = ctk.CTkLabel(contact_frame, text=name, width=20)
        label_name.pack(side="left", padx=5)
        
        label_phone = ctk.CTkLabel(contact_frame, text=details["phone"], width=15)
        label_phone.pack(side="left", padx=5)
        
        button_update = ctk.CTkButton(contact_frame, text="Update", command=lambda n=name: update_contact(n))
        button_update.pack(side="right", padx=5)
        
        button_delete = ctk.CTkButton(contact_frame, text="Delete", command=lambda n=name: delete_contact(n))
        button_delete.pack(side="right", padx=5)

def search_contact():
    search_term = entry_search.get()
    for widget in frame_contact_list.winfo_children():
        widget.destroy()
        
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["phone"]:
            contact_frame = ctk.CTkFrame(frame_contact_list)
            contact_frame.pack(pady=5, fill="x", padx=5)
            
            label_name = ctk.CTkLabel(contact_frame, text=name, width=20)
            label_name.pack(side="left", padx=5)
            
            label_phone = ctk.CTkLabel(contact_frame, text=details["phone"], width=15)
            label_phone.pack(side="left", padx=5)
            
            button_update = ctk.CTkButton(contact_frame, text="Update", command=lambda n=name: update_contact(n))
            button_update.pack(side="right", padx=5)
            
            button_delete = ctk.CTkButton(contact_frame, text="Delete", command=lambda n=name: delete_contact(n))
            button_delete.pack(side="right", padx=5)

def update_contact(name):
    def save_update():
        contacts[name] = {
            "phone": entry_update_phone.get(),
            "email": entry_update_email.get(),
            "address": entry_update_address.get()
        }
        messagebox.showinfo("Success", "Contact updated successfully!")
        top.destroy()
        display_contacts()
    
    top = ctk.CTkToplevel(app)
    top.title("Update Contact")
    top.geometry("600x400")
    
    label_update_phone = ctk.CTkLabel(top, text="Phone")
    label_update_phone.pack(pady=5)
    entry_update_phone = ctk.CTkEntry(top)
    entry_update_phone.pack(pady=5)
    entry_update_phone.insert(0, contacts[name]["phone"])
    
    label_update_email = ctk.CTkLabel(top, text="Email")
    label_update_email.pack(pady=5)
    entry_update_email = ctk.CTkEntry(top)
    entry_update_email.pack(pady=5)
    entry_update_email.insert(0, contacts[name]["email"])
    
    label_update_address = ctk.CTkLabel(top, text="Address")
    label_update_address.pack(pady=5)
    entry_update_address = ctk.CTkEntry(top)
    entry_update_address.pack(pady=5)
    entry_update_address.insert(0, contacts[name]["address"])
    
    button_save_update = ctk.CTkButton(top, text="Save", command=save_update)
    button_save_update.pack(pady=10)

def delete_contact(name):
    if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete contact '{name}'?"):
        del contacts[name]
        display_contacts()

# Create Tabs
tab_control = ctk.CTkTabview(app)
tab_add = tab_control.add("Add Contact")
tab_view = tab_control.add("View Contacts")
tab_control.pack(expand=1, fill="both")

# Add Contact Tab
label_name = ctk.CTkLabel(tab_add, text="Name")
label_name.pack(pady=5)
entry_name = ctk.CTkEntry(tab_add)
entry_name.pack(pady=5)

label_phone = ctk.CTkLabel(tab_add, text="Phone")
label_phone.pack(pady=5)
entry_phone = ctk.CTkEntry(tab_add)
entry_phone.pack(pady=5)

label_email = ctk.CTkLabel(tab_add, text="Email")
label_email.pack(pady=5)
entry_email = ctk.CTkEntry(tab_add)
entry_email.pack(pady=5)

label_address = ctk.CTkLabel(tab_add, text="Address")
label_address.pack(pady=5)
entry_address = ctk.CTkEntry(tab_add)
entry_address.pack(pady=5)

button_add = ctk.CTkButton(tab_add, text="Add Contact", command=add_contact)
button_add.pack(pady=10)

# View Contacts Tab
label_search = ctk.CTkLabel(tab_view, text="Search by Name or Phone")
label_search.pack(pady=5)
entry_search = ctk.CTkEntry(tab_view)
entry_search.pack(pady=5)

button_search = ctk.CTkButton(tab_view, text="Search", command=search_contact)
button_search.pack(pady=10)

frame_contact_list = ctk.CTkScrollableFrame(tab_view)
frame_contact_list.pack(expand=1, fill="both", pady=10, padx=10)

app.mainloop()
