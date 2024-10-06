import customtkinter

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue") #blue green & dark-blue

root = customtkinter.CTk()
root.geometry("600x500")
root.title("The Green Box")

boxes = []

def add_puo():
    boxes.append(user_input.get())
    user_input.delete('0', 'end')
    for box in boxes:
        print(box)



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="PUO finder")
label.pack(pady=12, padx=10)


user_input = customtkinter.CTkEntry(master=frame, placeholder_text="Enter PUO")
user_input.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Lägg till", command=add_puo)
button.pack(pady=12, padx=10)

root.mainloop()