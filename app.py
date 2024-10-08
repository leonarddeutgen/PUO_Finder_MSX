import customtkinter
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue") #blue green & dark-blue

root = customtkinter.CTk()
root.geometry("600x500")
root.title("The Green Box")
class puoBox:
    def __init__(self, puo_number, box_number, selected):
        self.number = puo_number
        self.box_number = box_number
        self.selected = selected

boxes = [puoBox("", i+1, False) for i in range(20)]

def render_boxes():
    for widget in boxes_container.winfo_children():
        widget.destroy()

    for i, box in enumerate(boxes):
        row = i // 5 
        col = i % 5 

        if box.selected == True:
            puo_box = customtkinter.CTkFrame(master=boxes_container, width=100, height=100, border_width=3, border_color="green")
        else:
            puo_box = customtkinter.CTkFrame(master=boxes_container, width=100, height=100)

        puo_box.grid(row=row, column=col, pady=12, padx=10)

        puo_label = customtkinter.CTkLabel(master=puo_box, text=box.number)
        puo_label.pack(pady=12, padx=10)

        puo_index = customtkinter.CTkLabel(master=puo_box, text=f"Box: {box.box_number}")
        puo_index.pack(pady=12, padx=10)

        remove_button = customtkinter.CTkButton(master=puo_box, text="Remove", command=lambda i=i: remove_puo(i))
        remove_button.pack(pady=12, padx=10, expand=True)

def add_puo():
    for box in boxes:
        if box.number == "":
            box.number = user_input.get()
            user_input.delete(0, "end")
            render_boxes()
            return
    messagebox.showwarning("Message", "No empty box were found")
    user_input.delete(0, "end")

def search_puo():
    for box in boxes:
        if box.number == user_input.get():
            box.selected = True
            user_input.delete(0, "end")
            render_boxes()
            return
    messagebox.showinfo("Message", "PUO not found :(")

def remove_puo(index):
    boxes[index].selected = False
    boxes[index].number = ""
    render_boxes()

app_container = customtkinter.CTkFrame(master=root)
app_container.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=app_container, text="PUO finder")
label.pack(pady=12, padx=10)

boxes_container = customtkinter.CTkFrame(master=app_container)
boxes_container.place(relx=0.05, rely=0.25, relwidth=0.90, relheight=0.80)  

user_input = customtkinter.CTkEntry(master=app_container, placeholder_text="Enter PUO")
user_input.pack(pady=12, padx=10)

add_button = customtkinter.CTkButton(master=app_container, text="Add PUO", command=add_puo)
add_button.pack(pady=12, padx=10)

search_button = customtkinter.CTkButton(master=app_container, text="Search", command=search_puo)
search_button.pack(pady=12, padx=10)

render_boxes()
root.mainloop()